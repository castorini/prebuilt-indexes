# Index READMEs

Build and usage documentation for the prebuilt indexes is maintained in this directory.

Find the README for an index through the **[Lucene catalog](../catalog/lucene.md)** or **[Faiss catalog](../catalog/faiss.md)**.

## Directory layout

READMEs are grouped by backend, then collection:

```text
index-readmes/
├── README.md
├── lucene/
│   ├── beir/
│   ├── bright/
│   ├── msmarco-v1/
│   ├── msmarco-v2/
│   ├── msmarco-v2.1/
│   └── ...
└── faiss/
    ├── beir/
    ├── cast2019/
    ├── miracl/
    ├── msmarco-v1/
    └── ...
```

Keep descriptive filenames so different models and build versions remain distinguishable. Shared READMEs within a collection are stored once.

## Add or update a README

For the workflow, see [Adding a prebuilt index](../../README.md#adding-a-prebuilt-index).

1. Add a Markdown file under `<backend>/<collection>/`, or edit an existing README directly. Include the corpus, model, build details, and usage instructions where applicable. Preserve attribution and license notices when adapting existing documentation.
2. Set `readme_local` on the corresponding index entry in `lucene/*.json` or `faiss/*.json`. The path is relative to `docs/index-readmes/`:

   ```json
   "readme_local": "lucene/example-collection/example-index.README.md"
   ```

   Multiple indexes can share the same path. Preserve the existing `readme` field for downstream software. If no local README is available, omit `readme_local`; the catalog displays a dash (—).
3. Regenerate and check the catalog:

   ```bash
   python scripts/generate_catalog.py
   python scripts/generate_catalog.py --check
   ```

The generator checks that each `readme_local` path points to a file within this directory and updates the catalog links.
