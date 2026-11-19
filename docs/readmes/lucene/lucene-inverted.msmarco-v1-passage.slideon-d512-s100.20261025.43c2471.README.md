# SlideOn d512/s100 Index for MS MARCO V1 Passage

This is a single-segment Lucene impact index containing 8,841,823 MS MARCO V1 passages.
It uses official precomputed SlideOn document vectors, not locally ONNX-encoded documents.

## Source and build

The source is [lightonai/SlideOn-sparse-vectors](https://huggingface.co/datasets/lightonai/SlideOn-sparse-vectors/tree/96e5ef60b4c4edef039693371c192157361adccf), revision `96e5ef6`.
The upstream document vectors are unscaled floating-point values.
We retained the first 512 entries of each stored descending-weight vector, multiplied weights by 100 in float32, rounded ties to even, and discarded zero integer weights before indexing.

The index was built on 2026-10-25 using Python 3.12.3, Java 21, Pyserini 0.44.0, Anserini 0.39.0, and Lucene 9.9.1.
The filename suffix identifies the existing Anserini release tag [anserini-0.39.0](https://github.com/castorini/anserini/releases/tag/anserini-0.39.0), commit [43c2471](https://github.com/castorini/anserini/commit/43c2471eb03f88164a49cd377d223b0065030374), not a new build or PR commit.
The build JAR SHA256 is `02e06f2f112803aeee9cb0a577b2e04edfa75a1318746a7fa5b6f802b2c6b14f`.

Equivalent conversion and indexing commands are shown below, using the pinned upstream [to_anserini.py](https://huggingface.co/datasets/lightonai/SlideOn-sparse-vectors/blob/96e5ef60b4c4edef039693371c192157361adccf/to_anserini.py).
The actual build used a local streaming converter implementing the same prefix-512/scale-100 conversion.
Paths are illustrative.

```bash
python /path/to/to_anserini.py \
  /path/to/msmarco-passage/corpus \
  /path/to/converted-corpus/part0.jsonl.gz \
  --k 512 --scale 100

java --add-modules=jdk.incubator.vector -Xmx4g \
  -cp /path/to/anserini-0.39.0-fatjar.jar io.anserini.index.IndexCollection \
  -collection JsonVectorCollection \
  -input /path/to/converted-corpus \
  -index indexes/lucene-inverted.msmarco-v1-passage.slideon-d512-s100.20261025.43c2471 \
  -generator DefaultLuceneDocumentGenerator \
  -threads 16 -impact -pretokenized -optimize
```

## Packaging and verification

The archive root directory matches the archive filename without `.tar.gz`.
Repackaging changes only the archive layout and metadata; the Lucene payload files are unchanged.
The index is shared by MS MARCO passage dev, DL19 passage, and DL20 passage evaluations.
Query pruning, including q64, is a query-side setting and is not baked into this document index.

```bash
sha256sum -c SHA256SUMS
md5sum -c MD5SUMS
```

## Original source

- [Original documentation](https://huggingface.co/datasets/castorini/prebuilt-indexes-msmarco-v1/blob/95b87294d8e858852e0d2352788ffe9658557e2e/passage/original/lucene-inverted/slideon/lucene-inverted.msmarco-v1-passage.slideon-d512-s100.20261025.43c2471.README.md)
