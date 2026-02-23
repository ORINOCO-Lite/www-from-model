"""Process project records into project pages

Needs the associated_with property on a project to be inlined to
correctly assign contributors and sites. Needs the (inverse of)
influenced_by field from the umbrella project to be joined to the
record (as "x_had_influence") to correctly assign roles.

"""

import json
from pathlib import Path
import re
import textwrap

import click
import yaml

SITE_DICT = {
    "ror:04xfq0f34": "aachen",  # RWTH Aachen
    "ror:04cvxnb49": "frankfurt",  # Goethe University Frankfurt
    "ror:038t36y30": "heidelberg",  # Heidelberg University
    "ror:02nv7yv05": "juelich",  # Forschungszentrum Jülich
    "ror:023b0x485": "mainz",  # Johannes Gutenberg University Mainz
    "ror:01hynnt93": "mannheim",  # CIMH Mannheim
    "ror:00fbnyb24": "wuerzburg",  # University of Würzburg
}


def format_title(d: dict) -> str | None:
    """Return formatted title

    Combines short name and title if possible. Makes do with what's
    available otherwise.

    """
    if "short_name" in d and "title" in d:
        res = f"{d['short_name']}: {d['title']}"
    elif "title" in d:
        res = d["title"]
    elif "short_name" in d:
        res = d["short_name"]
    else:
        res = None
    return res


def get_contributors_and_sites(d: dict) -> tuple[list[str], list[str]]:
    """Go through attributions, return contributor and site labels

    Only contributors with TRR root PID and known sites are returned.

    """
    ctb_pat = re.compile(r"trr379root:contributors/([\w\-]+)")
    contributors = set()
    sites = set()
    for association in d.get("associated_with", []):
        obj = association.get("object")
        roles = set(x if isinstance(x, str) else x.get("pid") for x in association.get("roles", []))
        if not isinstance(obj, dict):
            # silently demand inlined input so we can check schema type
            continue

        if obj.get("schema_type") == "trr379ri:TRR379Organization" and "marcrel:sht" in roles:
            # associated_with(org, supporting host) -> site
            if (site_label := SITE_DICT.get(obj["pid"])) is not None:
                sites.add(site_label)
        elif obj.get("schema_type") == "trr379ri:TRR379Person":
            # associated_with(person, any) -> contributor
            if (m := re.match(ctb_pat, obj["pid"])) is not None:
                contributors.add(m.group(1))

    return sorted(list(contributors)), sorted(list(sites))


def get_topics(d: dict) -> list[str]:
    topic_pat = re.compile(r"trr379root:topics/([\w\-]+)")
    topics = []
    for x in d.get("about", []):
        x_pid = x if isinstance(x, str) else x.get("pid")
        if (m := re.match(topic_pat, x_pid)) is not None:
            topics.append(m.group(1))
    return topics


def get_roles(d: dict) -> list[str]:
    """Get roles of the project

    A role of the project is defined by its influence on the TRR
    umbrella project. For this reason, we rely on the association
    class in the umbrella project's "influenced_by" to have been
    processed. We will assume that the result was appended as
    "x_had_influence" property on any given project.

    """
    pat = re.compile(r"trr379root:roles/([\w\-]+)")
    roles = set()
    for influence in d.get("x_had_influence", []):
        # we could check subject of that influence, but we accept any
        for role in influence.get("roles", []):
            role_pid = role if isinstance(role, str) else role.get("pid")
            if (m := re.match(pat, role_pid)) is not None:
                roles.add(m.group(1))
    return sorted(list(roles))


def get_weight(d: dict) -> int | None:
    """Return sorting weight, following existing convention"""
    pat = re.compile(r"trr379root:projects/([a-cq])(\d+)")
    major_weights = {"a": 1000, "b": 2000, "c": 3000, "q": 4000}
    if (m := re.match(pat, d["pid"])) is not None:
        return major_weights[m.group(1)] + (int(m.group(2)) - 1) * 10


def read_markdown_content(p: Path) -> tuple[dict | None, str | None]:
    """Read content from a markdown page with a yaml front matter"""
    with p.open() as fp:
        lines = fp.readlines()
    fence_loc = [i for i, line in enumerate(lines) if line.rstrip() == "---"]

    if len(fence_loc) >= 2:
        header_str = "".join(lines[fence_loc[0]+1:fence_loc[1]])
        content = "".join(lines[fence_loc[1]+1:])
        try:
            header = yaml.safe_load(header_str)
        except yaml.YAMLError:
            header = None
    else:
        header = None
        content = None

    return header, content


def write_page(p: Path, fm: dict, content: str | None, sep=True):
    """Write a markdown page with yaml front matter"""

    with p.open("wt") as fp:
        fp.write("---\n")
        yaml.dump(fm, stream=fp, allow_unicode=True, sort_keys=False)
        fp.write("---\n")
        if content is not None:
            if sep:
                fp.write("\n")
            fp.write(content)


@click.command()
@click.argument("input", type=click.File("rb"))
@click.argument(
    "outdir",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
)
def main(input, outdir):

    pat = re.compile(r"(https://trr379\.de/|trr379root:)projects/([\w\-]+)")

    for line in input:
        project = json.loads(line)

        if (m := re.match(pat, project["pid"])) is not None:
            label = m.group(2)
        else:
            # stick to trr379root:projects/ namespace (excludes root project)
            continue

        front_matter_dict = {}

        title = format_title(project)
        if title is not None:
            front_matter_dict["title"] = title

        contributors, sites = get_contributors_and_sites(project)
        if len(contributors) > 0:
            front_matter_dict["contributors"] = contributors
        if len(sites) > 0:
            front_matter_dict["sites"] = sites

        topics = get_topics(project)
        if len(topics) > 0:
            front_matter_dict["topics"] = topics

        roles = get_roles(project)
        if len(roles) > 0:
            front_matter_dict["roles"] = roles

        weight = get_weight(project)
        if weight is not None:
            front_matter_dict["weight"] = weight

        description = project.get("description")
        
        # prepare for writing markdown page(s)
        out_file = outdir / label / "_index.md"
        if not out_file.parent.is_dir():
            out_file.parent.mkdir()

        # write default (English) page
        write_page(
            out_file,
            front_matter_dict,
            (
                textwrap.fill(description, width=80, break_long_words=False)
                if description is not None
                else None
            ),
        )

        # for German, keep description and title from the old file, update header
        # (until internationalization is solved in the Pool)
        out_file_de = out_file.with_suffix(".de.md")
        if out_file_de.exists():
            old_header_de, old_content_de, = read_markdown_content(out_file_de)
        else:
            old_header_de = old_content_de = None

        new_header_de = front_matter_dict.copy()
        if old_header_de is not None and "title" in old_header_de:
            new_header_de["title"] = old_header_de["title"]
        write_page(out_file_de, new_header_de, old_content_de, sep=False)


if __name__ == "__main__":
    main()
