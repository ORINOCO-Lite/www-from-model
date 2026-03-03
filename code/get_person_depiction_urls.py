#!/usr/bin/env python3
"""Generate person-depiction-distribution-urls
"""
import sys
import json
from urllib.parse import urlparse, unquote
from pathlib import Path

def get_extension(url):
    """
    Extract the file extension from a URL.
    Ignores query parameters and fragments.
    """
    path = urlparse(url).path
    return Path(unquote(path)).suffix.lstrip('.')

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        person = json.loads(line)
    except json.JSONDecodeError:
        # skip invalid JSON
        continue

    pid = person.get("pid")
    if not pid:
        continue
    curie_ref = pid.split(":", 1)[-1]

    depictions = person.get("depictions", [])
    for dep in depictions:
        if dep.get("kind") != "xyzrins:depiction-types/e9a34f7d-d05e-4591-bb45-f8a0c499e07b":
            continue
        distributions = dep.get("distributions", [])
        for dist in distributions:
            for char in dist.get("characterized_by", []):
                if char.get("predicate") != "dcat:downloadUrl":
                    continue
                url = char.get("object")
                if not url:
                    continue
                ext = get_extension(url)
                print(f"{curie_ref}\t{ext}\t{url}")