<img src="docs/pyserini-logo-small.png" width="200" />

# Prebuilt Indexes for Anserini and Pyserini

This repository provides the source of truth for prebuilt indexes used by [Anserini](http://anserini.io/) and [Pyserini](http://pyserini.io/).

## Browse indexes

Indexes are organized by backend and collection.

Browse index IDs, Hugging Face links, and [locally stored index READMEs](docs/index-readmes/README.md). Each collection links to its metadata JSON for descriptions, sizes, checksums, and download URLs:

- **[Lucene indexes](docs/catalog/lucene.md)**: inverted, impact, flat vector, and HNSW indexes.
- **[Faiss indexes](docs/catalog/faiss.md)**: dense vector indexes.

For usage instructions, see [Anserini](https://github.com/castorini/anserini/blob/master/docs/prebuilt-indexes.md) and [Pyserini](https://github.com/castorini/pyserini/blob/master/docs/prebuilt-indexes.md). Available index IDs depend on the metadata version pinned by your installed software. Index files remain at their existing hosting locations.

## Source metadata

+ Metadata for Lucene indexes is stored in [`lucene/`](https://github.com/castorini/prebuilt-indexes/tree/main/lucene).
+ Metadata for Faiss indexes is stored in [`faiss/`](https://github.com/castorini/prebuilt-indexes/tree/main/faiss).

## Adding a prebuilt index

Publish the index artifact, register its metadata, and add its documentation to make it discoverable in the [Lucene](docs/catalog/lucene.md) or [Faiss](docs/catalog/faiss.md) catalog.

```text
Publish index artifact (Hugging Face or another host)
    ↓
Add a README under docs/index-readmes/<backend>/<collection>/
    ↓
Add index metadata with readme_local; regenerate manifests if needed
    ↓
Generate and check the catalog → Submit a pull request
```

Run all commands below from the repository root.

## Updating the catalog

The catalog is generated from the metadata; do not edit its Markdown pages directly.
Index READMEs are maintained directly in `docs/index-readmes/`. Each index's optional `readme_local` metadata field specifies its README path relative to that directory. See [README maintenance](docs/index-readmes/README.md#add-or-update-a-readme) for adding or updating them.
After changing metadata, regenerate it from the repository root:

```bash
python scripts/generate_catalog.py
```

To check generated pages without changing files:

```bash
python scripts/generate_catalog.py --check
```

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
