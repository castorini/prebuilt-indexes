# BRIGHT.bge-large-en-v1.5 (Flat)

Lucene flat dense vector indexes of BRIGHT corpora using BGE-large-en-v1.5.

These indexes were built 2025/08/19 on `basilisk` at Anserini commit [`e5ee76`](https://github.com/castorini/anserini/commit/e5ee760d7097193ba18f1e099f9f71c2940ae2ae).

Here is the command used:

```bash
CORPORA=(biology earth-science economics psychology robotics stackoverflow sustainable-living pony leetcode aops theoremqa-theorems theoremqa-questions); 
for c in "${CORPORA[@]}"
do
java -cp $ANSERINI_JAR --add-modules jdk.incubator.vector io.anserini.index.IndexFlatDenseVectors \
  -threads 16 \
  -collection JsonDenseVectorCollection \
  -input /store2/scratch/l2ge/bright/encode/bge-large-en-v1.5/$c \
  -generator DenseVectorDocumentGenerator \
  -index indexes/lucene-flat/$c/ -optimize
```

## Original source

- [Original documentation](https://huggingface.co/datasets/castorini/prebuilt-indexes-bright/blob/3d6370ba43a5f5b805eb8f544e1cf43ce472d702/lucene-flat/bge-large-en-v1.5/lucene-flat.bright.bge-large-en-v1.5.20250819.e5ee76.README.md)
