# msmarco-v1-passage-deepimpact

Lucene impact index of the MS MARCO V1 passage corpus for DeepImpact.

This index was generated on 2022/10/05 at Anserini commit [`252b5e`](https://github.com/castorini/anserini/commit/252b5e2087dd7b3b994d41a444d4ae0044519819) on `tuna` with the following command:

```bash
nohup target/appassembler/bin/IndexCollection \
 -collection JsonVectorCollection \
 -input /tuna1/collections/msmarco/msmarco-passage-deepimpact/ \
 -index indexes/lucene-index.msmarco-v1-passage-deepimpact.20221005.252b5e/ \
 -generator DefaultLuceneDocumentGenerator \
 -threads 16 -impact -pretokenized -optimize >& logs/log.msmarco-v1-passage-deepimpact.20221005.252b5e &
```

In April 2024, index was repackaged to adopt a more consistent naming scheme.

## Original source

- [Original documentation](https://huggingface.co/datasets/castorini/prebuilt-indexes-msmarco-v1/blob/95b87294d8e858852e0d2352788ffe9658557e2e/passage/original/lucene-inverted/deepimpact/lucene-inverted.msmarco-v1-passage.deepimpact.20221005.252b5e.README.md)
