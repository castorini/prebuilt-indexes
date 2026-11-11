# Index READMEs

Build and usage documentation for the prebuilt indexes is maintained in this directory.

Find the README for an index through the **[Lucene catalog](../catalog/lucene.md)** or **[Faiss catalog](../catalog/faiss.md)**.

## Directory layout

READMEs are grouped by backend:

```text
readmes/
├── README.md
├── lucene/
│   ├── lucene-hnsw.msmarco-v1-passage.cosdpr-distil.20240108.825148.README.md
│   └── ...
└── faiss/
    ├── faiss-hnsw.cast2019.tct_colbert-v2-readme.md
    └── ...
```

Keep descriptive filenames so different models and build versions remain distinguishable. Shared READMEs within a collection are stored once.

## Add or update a README

For the workflow, see [Adding a prebuilt index](../../README.md#adding-a-prebuilt-index).

1. Add a Markdown file under `docs/readmes/<backend>/`, or edit an existing README directly. Include the corpus, model, build details, and usage instructions where applicable. Preserve attribution and license notices when adapting existing documentation.
2. Set `readme` on the corresponding index entry in `lucene/*.json` or `faiss/*.json`. The path is relative to `docs/readmes/`:

   ```json
   "readme": "lucene/example-index.README.md"
   ```

   Multiple indexes can share the same path. If no README is available, omit `readme`; the catalog displays a dash (—). Some existing entries retain external URLs or unresolved filenames; these are not rendered as local README links.
3. Regenerate and check the catalog:

   ```bash
   python scripts/generate_catalog.py
   python scripts/generate_catalog.py --check
   ```

The generator checks that each local `readme` path points to a file within this directory and updates the catalog links.
