import json
from pprint import pprint
import sys

nodes = {}
edges = {}

wanted_node_types = {
    "xyzri:XYZInstrument": 'instrument',
    "xyzri:XYZOrganization": 'organization',
    "xyzri:XYZPerson": 'person',
    "xyzri:XYZProject": 'project',
    "xyzri:XYZPublication": 'publication',
    "xyzri:XYZTopic": 'topic',
    "xyzri:XYZObjective": 'objective',
}

wanted_edge_types = {
    'associated_with': 'associated_with',
    'attributed_to': 'attributed_to',
    'generated_by': 'generated_by',
    'delegated_by': 'delegated_by',
    'influenced_by': 'influenced_by',
    'part_of': 'part_of',
    'about': 'about',
}


def get_node_label(rec: dict) -> str | None:
    for src in (
        'short_name',
        'name',
        'title',
        'family_name',
    ):
        label = rec.get(src)
        if label:
            if src == 'family_name':
                return f'{rec["given_name"][0]}.{label}'
            else:
                return label
    return None


def get_node_url(rec: dict) -> str | None:
    pid = rec['pid']
    www_root_prefix = 'xyzrins:'
    if pid.startswith(www_root_prefix):
        return f'/{pid[len(www_root_prefix):]}'
    return None


def add_edge(src: str, target: str, kind: str) -> None:
    # use the edge properties as ID to get auto-deduplication
    edge_id = (src, target)
    edges[edge_id] = {
        'id': edge_id,
        'source': src,
        'target': target,
    }


for line in sys.stdin:
    rec = json.loads(line)
    schema_type = rec.get('schema_type')
    if schema_type not in wanted_node_types:
        continue

    pid = rec['pid']
    if pid in nodes:
        print(f'Ignoring duplicate node {pid}', file=sys.stderr)
        continue

    for prop, edge_kind in wanted_edge_types.items():
        for rel in rec.get(prop, []):
            obj = rel['object'] if isinstance(rel, dict) else rel
            add_edge(pid, obj, edge_kind)

    nodes[pid] = {
        'id': pid,
        'label': get_node_label(rec),
        'type': wanted_node_types[schema_type],
        'size': 1,
        'url': get_node_url(rec),
    }

kept_edges = []
nodes_missing = set()
for edge in edges.values():
    err = False
    for prop in ('source', 'target'):
        if edge[prop] not in nodes:
            nodes_missing.add(edge[prop])
            err = True
    if err:
        continue
    nodes[edge['target']]['size'] += 1
    kept_edges.append(edge)

out = {'nodes': list(nodes.values()), 'edges': kept_edges}

json.dump(out, sys.stdout)

if nodes_missing:
    pprint(
        f"Missing nodes: {nodes_missing!r}",
        stream=sys.stderr,
    )
