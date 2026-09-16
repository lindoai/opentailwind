#!/usr/bin/env python3
"""Check the exported free selection, local catalogue, and optional LNUI source."""

import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path


class CatalogueLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = []

    def handle_starttag(self, tag, attrs):
        href = dict(attrs).get("href", "")
        if tag == "a" and href.startswith(("blocks/", "landings/")):
            self.paths.append(href)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="Path to the LNUI project")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    catalog = json.loads((root / "free-catalog.json").read_text())
    errors = []
    expected_links = []

    for folder, source_name in (
        ("blocks", "free-blocks.json"),
        ("landings", "free-templates.json"),
    ):
        ids = catalog[folder]
        expected = {f"{item.replace('/', '-')}.html" for item in ids}
        actual = {str(path.relative_to(root / folder)) for path in (root / folder).rglob("*") if path.is_file()}
        if len(set(ids)) != len(ids) or len(expected) != len(ids):
            errors.append(f"{folder}: duplicate IDs or filename collisions")
        if actual != expected:
            errors.append(f"{folder}: missing {sorted(expected - actual)}, unexpected {sorted(actual - expected)}")
        expected_links.extend(f"{folder}/{name}" for name in expected)

        if args.source:
            source_ids = set(json.loads((args.source / "src/data" / source_name).read_text()))
            if paid := set(ids) - source_ids:
                errors.append(f"{folder}: IDs not marked free in LNUI: {sorted(paid)}")
            if folder == "landings" and set(ids) != source_ids:
                errors.append("landings: export does not contain the complete free template selection")

    page = CatalogueLinks()
    page.feed((root / "index.html").read_text())
    if Counter(page.paths) != Counter(expected_links):
        errors.append("index.html: catalogue must link to every included design exactly once")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Verified {len(catalog['blocks'])} free blocks and {len(catalog['landings'])} free templates; all catalogue links match.")


if __name__ == "__main__":
    main()
