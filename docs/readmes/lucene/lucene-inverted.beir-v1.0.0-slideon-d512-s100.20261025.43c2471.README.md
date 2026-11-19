# BEIR (v1.0.0): SlideOn d512/s100 Lucene impact indexes

The upstream SlideOn dataset provides **unscaled floating-point document vectors**.
We converted those vectors into **scale-100 integer impacts locally** to build these Lucene indexes.

## Source and build

- Vectors: [lightonai/SlideOn-sparse-vectors](https://huggingface.co/datasets/lightonai/SlideOn-sparse-vectors/tree/96e5ef60b4c4edef039693371c192157361adccf),
  revision `96e5ef6`.
- Our preprocessing: keep the first 512 entries of each upstream descending-weight
  document vector, convert with float32 `np.rint(weight * 100)` (ties-to-even), and
  remove zeros. This conversion is performed before indexing, not by the model.
- The upstream [`to_anserini.py`](https://huggingface.co/datasets/lightonai/SlideOn-sparse-vectors/blob/96e5ef60b4c4edef039693371c192157361adccf/to_anserini.py)
  provides this integer conversion with `--scale` defaulting to 100.
- Build dates from index logs: **2026-10-25**, except BioASQ (**2026-10-26**).
- Python 3.12.3, Java 21, Pyserini 0.44.0, Anserini **0.39.0**, Lucene **9.9.1**.
- Anserini release tag [`anserini-0.39.0`](https://github.com/castorini/anserini/releases/tag/anserini-0.39.0) resolves to [`43c2471`](https://github.com/castorini/anserini/commit/43c2471eb03f88164a49cd377d223b0065030374).
  The filename suffix identifies this existing release tag, not a new build or PR commit.
- Exact build JAR SHA256:
  `02e06f2f112803aeee9cb0a577b2e04edfa75a1318746a7fa5b6f802b2c6b14f`.
- `JsonVectorCollection`, `DefaultLuceneDocumentGenerator`, `-impact -pretokenized -optimize`.
  Each index has one segment. Four indexing threads were used, except SciFact (16).

Equivalent conversion and indexing commands (paths are illustrative). Use
`to_anserini.py` from the pinned upstream revision above; the corpus directory
contains the dataset's `part-*.parquet` document vectors.

The actual build used a local streaming converter implementing the same
prefix-512 / scale-100 conversion. The upstream command below expresses that
conversion without requiring our local orchestration scripts.

```bash
# Convert document vectors to JsonVectorCollection input (not query mode).
python /path/to/to_anserini.py \
  /path/to/dataset/corpus \
  /path/to/converted-corpus/part0.jsonl.gz \
  --k 512 --scale 100

# Build the single-segment Lucene impact index.
# Use -threads 16 for SciFact to match its build settings.
java --add-modules=jdk.incubator.vector -Xmx4g \
  -cp /path/to/anserini-0.39.0-fatjar.jar io.anserini.index.IndexCollection \
  -collection JsonVectorCollection -input /path/to/converted-corpus \
  -index /path/to/index -generator DefaultLuceneDocumentGenerator \
  -threads 4 -impact -pretokenized -optimize
```

## Packaging and verification

Target directory: `lucene-inverted/slideon/` in
[`castorini/prebuilt-indexes-beir`](https://huggingface.co/datasets/castorini/prebuilt-indexes-beir).

```bash
sha256sum -c SHA256SUMS
md5sum -c MD5SUMS
```

## Scope

This folder contains **29 BEIR subcollections**: 17 standalone collections and
12 CQADupStack subsets. MS MARCO is not included. The additional BioASQ, Robust04,
Signal-1M and TREC-News indexes were not part of the ONNX query-side BEIR-15 evaluation.

| Collection | Documents | Archive MiB |
|---|---:|---:|
| arguana | 8,674 | 6.0 |
| bioasq | 14,914,603 | 9073.4 |
| climate-fever | 5,416,593 | 3312.2 |
| cqadupstack-android | 22,998 | 13.0 |
| cqadupstack-english | 40,221 | 22.3 |
| cqadupstack-gaming | 45,301 | 25.5 |
| cqadupstack-gis | 37,637 | 22.4 |
| cqadupstack-mathematica | 16,705 | 10.2 |
| cqadupstack-physics | 38,316 | 22.9 |
| cqadupstack-programmers | 32,176 | 19.8 |
| cqadupstack-stats | 42,269 | 25.2 |
| cqadupstack-tex | 68,184 | 39.9 |
| cqadupstack-unix | 47,382 | 27.9 |
| cqadupstack-webmasters | 17,405 | 10.5 |
| cqadupstack-wordpress | 48,605 | 28.0 |
| dbpedia-entity | 4,635,922 | 2967.0 |
| fever | 5,416,568 | 3312.2 |
| fiqa | 57,638 | 35.1 |
| hotpotqa | 5,233,329 | 3037.0 |
| nfcorpus | 3,633 | 2.6 |
| nq | 2,681,468 | 1567.5 |
| quora | 522,931 | 111.8 |
| robust04 | 528,155 | 331.1 |
| scidocs | 25,657 | 18.3 |
| scifact | 5,183 | 3.6 |
| signal1m | 2,866,316 | 1022.7 |
| trec-covid | 171,332 | 93.6 |
| trec-news | 594,977 | 401.1 |
| webis-touche2020 | 382,545 | 210.3 |

## Original source

- [Original documentation](https://huggingface.co/datasets/castorini/prebuilt-indexes-beir/blob/873a3d8a8be36494ff1079387d141c523a6ac7cf/lucene-inverted/slideon/lucene-inverted.beir-v1.0.0-slideon-d512-s100.20261025.43c2471.README.md)
