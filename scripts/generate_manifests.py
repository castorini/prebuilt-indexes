#!/usr/bin/env python3
"""Generate or check the Lucene and Faiss metadata manifests."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="Check manifests without modifying files."
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    stale = False

    for directory in ("lucene", "faiss"):
        folder = root / directory
        manifest = folder / "manifest.json"
        filenames = sorted(
            path.name
            for path in folder.glob("*.json")
            if path.is_file() and path != manifest
        )
        expected = json.dumps(filenames, indent=2) + "\n"
        relative_path = manifest.relative_to(root)

        if args.check:
            if not manifest.is_file() or manifest.read_text(encoding="utf-8") != expected:
                print(f"Stale or missing manifest: {relative_path}")
                stale = True
        else:
            manifest.write_text(expected, encoding="utf-8")
            print(f"Generated {relative_path} ({len(filenames)} files)")

    if stale:
        print("Run python3 scripts/generate_manifests.py to regenerate manifests.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
