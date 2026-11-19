# msmarco-v2.1-arctic-embed-l

Faiss FlatIP indexes of msmarco v2.1 encoded by Snowflake embed-l. These indexes were generated on 2024/08/26 on `orca`.

The indexes were generated from indexing embeddings available on [Huggingface](https://huggingface.co/datasets/Snowflake/msmarco-v2.1-snowflake-arctic-embed-l).

## Preparation
Due to msmarco v2.1 dataset's large size, indexes needed to be divided in two parts.

```bash
python scripts/arctic/convert_embeddings.py --embeddings_folder /store/scratch/sjupadhy/msmarco-v2.1-snowflake-arctic-embed-l/corpus \
--output /store/scratch/sjupadhy/indexes/msmarco-v2.1-dev-snowflake-arctic-embed-l-1 \
--indices 0_30

python scripts/arctic/convert_embeddings.py --embeddings_folder /store/scratch/sjupadhy/msmarco-v2.1-snowflake-arctic-embed-l/corpus \
--output /store/scratch/sjupadhy/indexes/msmarco-v2.1-dev-snowflake-arctic-embed-l-2 \
--indices 30_59
```

### Topic embeddings
```bash
python scripts/arctic/convert_queries.py --embedding_path /store/scratch/sjupadhy/msmarco-v2.1-snowflake-arctic-embed-l/topics/snowflake-arctic-embed-l-topics.msmarco-v2-doc.dev.parquet \
--output /store/scratch/sjupadhy/queries/msmarco-v2.1-dev-snowflake-arctic-embed-l

```

## Original source

- [Original documentation](https://github.com/castorini/pyserini/blob/19486954995f4517c670881145caf2f284f3be22/pyserini/resources/index-metadata/faiss-flat.msmarco-v2.1-doc.arctic-embed-l.20240824.README.md)
