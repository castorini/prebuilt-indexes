<img src="docs/pyserini-logo-small.png" width="200" />

# Prebuilt Index Metadata for Anserini and Pyserini

This repository provides the source of truth for prebuilt indexes used by [Anserini](http://anserini.io/) and [Pyserini](http://pyserini.io/).

+ Metadata for Lucene indexes is stored in [`lucene/`](https://github.com/castorini/prebuilt-indexes/tree/main/lucene).
+ Metadata for Faiss indexes is stored in [`faiss/`](https://github.com/castorini/prebuilt-indexes/tree/main/faiss).

## Metadata manifests

Each metadata directory contains a `manifest.json` listing its metadata JSON filenames in sorted order, relative to that directory.
The manifest excludes itself.

After adding, removing, or renaming metadata files, regenerate both manifests from the repository root:

```bash
python scripts/generate_manifests.py
```

To check that both manifests are up to date without modifying files:

```bash
python scripts/generate_manifests.py --check
```

This check also runs in GitHub Actions on pushes and pull requests.
