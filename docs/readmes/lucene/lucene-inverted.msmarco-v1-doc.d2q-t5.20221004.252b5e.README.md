# msmarco-v1-doc-d2q-t5

Lucene index of the MS MARCO V1 document corpus, with doc2query-T5 expansions.

Note that there are two variants:

+ `msmarco-v1-doc-d2q-t5` (2.1G uncompressed): stores term frequencies only, which supports bag-of-words queries, but no phrase queries and no relevance feedback. There is no way to fetch the raw text.
+ `msmarco-v1-doc-d2q-t5-docvectors` (12G uncompressed): stores term frequencies and the docvectors, which enables pseudo-relevance feedabck.

These indexes were generated on 2022/10/04 at Anserini commit [`252b5e`](https://github.com/castorini/anserini/commit/252b5e2087dd7b3b994d41a444d4ae0044519819) on `tuna` with the following commands:

```
target/appassembler/bin/IndexCollection -collection JsonCollection \
  -generator DefaultLuceneDocumentGenerator -threads 7 \
  -input /tuna1/collections/msmarco/msmarco-doc-docTTTTTquery/ \
  -index indexes/lucene-index.msmarco-v1-doc-d2q-t5.20221004.252b5e/ \
  -optimize >& logs/log.msmarco-v1-doc-d2q-t5.20221004.252b5e &

target/appassembler/bin/IndexCollection -collection JsonCollection \
  -generator DefaultLuceneDocumentGenerator -threads 7 \
  -input /tuna1/collections/msmarco/msmarco-doc-docTTTTTquery/ \
  -index indexes/lucene-index.msmarco-v1-doc-d2q-t5-docvectors.20221004.252b5e/ \
  -storeDocvectors -optimize >& logs/log.msmarco-v1-doc-d2q-t5-docvectors.20221004.252b5e &
```

In April 2024, indexes were repackaged to adopt a more consistent naming scheme.

## Original source

- [Original documentation](https://huggingface.co/datasets/castorini/prebuilt-indexes-msmarco-v1/blob/95b87294d8e858852e0d2352788ffe9658557e2e/doc/d2q-t5/lucene-inverted/tf/lucene-inverted.msmarco-v1-doc.d2q-t5.20221004.252b5e.README.md)
