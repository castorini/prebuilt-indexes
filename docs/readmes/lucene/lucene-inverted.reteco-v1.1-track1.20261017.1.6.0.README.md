# RETECO v1.1: TRACK1 Lucene inverted indexes

Optimized Anserini Lucene inverted indexes of the official RETECO v1.1 corpus.
Source: [DataScience-UIBK/RETECO-SemEval2027](https://huggingface.co/datasets/DataScience-UIBK/RETECO-SemEval2027/tree/c21e10ba8aa60eaa201f60fc4604364469c5ec17); full revision `c21e10ba8aa60eaa201f60fc4604364469c5ec17`.
Track 1 is **deduplicated upstream**. No additional document deduplication or ID rewriting was applied during indexing. The same full domain index serves train and dev.

Built on `20261017` using Anserini **1.6.0** (fat JAR SHA-256 `b46c41046bc0c72048094d7bd34422276c04e9cef7ab25f76f5b8ea583c9aaf2`) and Java 21.0.10; the exact Anserini Git commit of this JAR is **not recorded and is not claimed**. The filename suffix `1.6.0` identifies the release, not a commit SHA.
Indexer: Anserini [`io.anserini.index.IndexCollection`](https://github.com/castorini/anserini/blob/master/src/main/java/io/anserini/index/IndexCollection.java) called through a local `IndexCollectionLargeStrings` wrapper, which only raises Jackson’s maximum JSON string length to preserve a very long HSM document. Options: `-collection JsonCollection -generator DefaultLuceneDocumentGenerator -threads 8 -storePositions -storeDocvectors -storeRaw -optimize`. Every published index was validated against the official document count, qrel IDs, and **one Lucene segment**.

## Indexes

| Domain | Documents | Archive | Size (bytes) | SHA-256 | MD5 |
|---|---:|---|---:|---|---|
| bitcoin | 76,706 | [lucene-inverted.reteco-v1.1-track1-bitcoin.20261017.1.6.0.tar.gz](lucene-inverted.reteco-v1.1-track1-bitcoin.20261017.1.6.0.tar.gz) | 175,529,303 | `5f2a39ab0b8d955f544cb80175322455675b5499019ebee38a9598622d6b90a7` | `7b260c67db7b32c3afee0fc22a8e6262` |
| cardano | 47,509 | [lucene-inverted.reteco-v1.1-track1-cardano.20261017.1.6.0.tar.gz](lucene-inverted.reteco-v1.1-track1-cardano.20261017.1.6.0.tar.gz) | 105,452,670 | `bd06fdc3e144274fad1093d700b7683a0c4f87cfb773f34eea776d6243bebf8f` | `9acab877867f8833860785c8a402c251` |
| economics | 74,692 | [lucene-inverted.reteco-v1.1-track1-economics.20261017.1.6.0.tar.gz](lucene-inverted.reteco-v1.1-track1-economics.20261017.1.6.0.tar.gz) | 183,682,895 | `71a38d39badf9b9525498bcb0074449181470e6c1d5e6e56335c91dac0a18f2b` | `2bac0ba43cd7f9c72e7f19ec1ba602d3` |
| genealogy | 136,101 | [lucene-inverted.reteco-v1.1-track1-genealogy.20261017.1.6.0.tar.gz](lucene-inverted.reteco-v1.1-track1-genealogy.20261017.1.6.0.tar.gz) | 369,336,128 | `f35ad8f18b1be7b35f607cbec858a761c3abf38b78e0144683a76fe63b581501` | `150998a97d373408757086d6baf27560` |
| history | 200,252 | [lucene-inverted.reteco-v1.1-track1-history.20261017.1.6.0.tar.gz](lucene-inverted.reteco-v1.1-track1-history.20261017.1.6.0.tar.gz) | 805,743,656 | `da3894b10f766de52d369780b3d221ef63307203c9d888baae5aeb20701d1f85` | `8eac11979e65e4b5b56df78745f79e54` |
| hsm | 169,552 | [lucene-inverted.reteco-v1.1-track1-hsm.20261017.1.6.0.tar.gz](lucene-inverted.reteco-v1.1-track1-hsm.20261017.1.6.0.tar.gz) | 442,465,076 | `86324f6f78dcb9e692bce198589d4368ba381ac12c62a33c7f6d7f08930115a2` | `1e1286f98480a30f2eb0dcdd4f77d37b` |
| iota | 9,680 | [lucene-inverted.reteco-v1.1-track1-iota.20261017.1.6.0.tar.gz](lucene-inverted.reteco-v1.1-track1-iota.20261017.1.6.0.tar.gz) | 34,011,796 | `00d4da261b4b0be7793fc2d72ed559b2991790ee2aea0dc30cdae102bbe16203` | `5fec2d2e72d29c4687ecbdbad1b8bf17` |
| law | 36,110 | [lucene-inverted.reteco-v1.1-track1-law.20261017.1.6.0.tar.gz](lucene-inverted.reteco-v1.1-track1-law.20261017.1.6.0.tar.gz) | 92,117,058 | `86d896c20b90e965e76b6836fa8dcef18c7af8ec67502a3c7db9df1ea3d730e4` | `e5e77b936dceac61170125b578d21da5` |
| monero | 53,955 | [lucene-inverted.reteco-v1.1-track1-monero.20261017.1.6.0.tar.gz](lucene-inverted.reteco-v1.1-track1-monero.20261017.1.6.0.tar.gz) | 135,537,781 | `1423792c8916db02dcaaa08cd243b0880825a7c8c0b0dc5022c799268703b143` | `e83a8742ad719692e1b95c2e73719d62` |
| politics | 135,207 | [lucene-inverted.reteco-v1.1-track1-politics.20261017.1.6.0.tar.gz](lucene-inverted.reteco-v1.1-track1-politics.20261017.1.6.0.tar.gz) | 359,293,115 | `89a610aca06f39af8802282d0f3c15ac5ea1dffb902b52c941fedcbe1d83ac94` | `1bd17af5ac63d1828e854947643cfd69` |
| quant | 25,040 | [lucene-inverted.reteco-v1.1-track1-quant.20261017.1.6.0.tar.gz](lucene-inverted.reteco-v1.1-track1-quant.20261017.1.6.0.tar.gz) | 55,059,609 | `16a3b05d8053b6cb5c9ffdf6f5288961310c6e17e9b060d369753fa0da5c6572` | `86e39f8fabac5c7c3cde9230aa5eb601` |
| travel | 158,771 | [lucene-inverted.reteco-v1.1-track1-travel.20261017.1.6.0.tar.gz](lucene-inverted.reteco-v1.1-track1-travel.20261017.1.6.0.tar.gz) | 320,076,049 | `ca06d6581db7873bda02b02cb41b176010fbae3bb528226887de2bffcc251695` | `41bbd090b4e4b46439c47b85849192a1` |
| workplace | 43,584 | [lucene-inverted.reteco-v1.1-track1-workplace.20261017.1.6.0.tar.gz](lucene-inverted.reteco-v1.1-track1-workplace.20261017.1.6.0.tar.gz) | 86,471,386 | `c58f837b5e6508a31a4a051ce0c4fa6cf567e4e6d6e22f84cb4f92cceaea6771` | `d6c134d50638fdd967e82194a1d91b6c` |

## Reproduce the indexes

The following commands reproduce the build using the official pinned v1.1 release and Anserini 1.6.0. They do not use or modify any existing RETECO index. The archive contains Lucene indexes, not the source corpus.

```bash
hf download DataScience-UIBK/RETECO-SemEval2027 --repo-type dataset --revision c21e10ba8aa60eaa201f60fc4604364469c5ec17 --include "track1_tempo/*/documents.jsonl" --include "track1_tempo/*/qrels_*.txt" --include "split_manifest.json" --local-dir reteco_data
```

Convert `{ "id": ..., "content": ... }` into Anserini `JsonCollection` rows `{ "id": ..., "contents": ... }`, keeping every ID and full text unchanged:

```python
import json
from pathlib import Path
sources = sorted(Path("reteco_data/track1_tempo").glob("*/documents.jsonl"))
assert len(sources) == 13
for source in sources:
    output = Path("collections/track1_tempo") / source.parent.name / "docs.jsonl"
    output.parent.mkdir(parents=True, exist_ok=True)
    ids = set()
    with source.open(encoding="utf-8") as src, output.open("w", encoding="utf-8") as dst:
        for line in src:
            row = json.loads(line)
            if row["id"] in ids: raise ValueError(row["id"])
            ids.add(row["id"])
            dst.write(json.dumps({"id": row["id"], "contents": row["content"]}, ensure_ascii=False) + "\n")
```

Save the Python block as `convert.py` and run `python3 convert.py`. The Java wrapper below **only** raises Jackson’s JSON string limit; it is necessary for the very long HSM document. Save it as `IndexCollectionLargeStrings.java`:

```java
import com.fasterxml.jackson.core.StreamReadConstraints;
import io.anserini.index.IndexCollection;
public final class IndexCollectionLargeStrings {
  public static void main(String[] args) throws Exception {
    StreamReadConstraints.overrideDefaultStreamReadConstraints(
        StreamReadConstraints.builder().maxStringLength(256 * 1024 * 1024).build());
    IndexCollection.main(args);
  }
}
```

Here is the **actual IndexCollection invocation**, including `-optimize`, for all 13 domains. The Python check prevents publishing incomplete indexes even if Java exits successfully:

```bash
set -euo pipefail
JAR=/path/to/anserini-1.6.0-fatjar.jar
mkdir -p classes indexes/reteco-v1.1/track1_tempo logs
javac -proc:none -cp "$JAR" -d classes IndexCollectionLargeStrings.java
for domain in bitcoin cardano economics genealogy history hsm iota law monero politics quant travel workplace; do
  test ! -e "indexes/reteco-v1.1/track1_tempo/$domain"
  test ! -e "indexes/reteco-v1.1/track1_tempo/$domain.building"
  java -Xmx16g -cp "classes:$JAR" IndexCollectionLargeStrings \
    -collection JsonCollection \
    -input "collections/track1_tempo/$domain" \
    -index "indexes/reteco-v1.1/track1_tempo/$domain.building" \
    -generator DefaultLuceneDocumentGenerator -threads 8 \
    -storePositions -storeDocvectors -storeRaw -optimize \
    > "logs/$domain.log" 2>&1
  python3 - "$domain" <<'PY'
import json, sys
from pathlib import Path
from pyserini.search.lucene import LuceneSearcher
domain = sys.argv[1]
source = Path("reteco_data/track1_tempo") / domain
expected = json.loads(Path("reteco_data/split_manifest.json").read_text())["track1_tempo"][domain]["documents"]
index = Path("indexes/reteco-v1.1/track1_tempo") / (domain + ".building")
searcher = LuceneSearcher(str(index))
assert searcher.index_reader.stats()["documents"] == expected
assert searcher.object.reader.leaves().size() == 1
for split in ("train", "dev"):
    for row in (source / f"qrels_{split}.txt").read_text().splitlines():
        if int(row.split()[3]) > 0:
            assert searcher.doc(row.split()[2]) is not None, row
PY
  mv "indexes/reteco-v1.1/track1_tempo/$domain.building" \
     "indexes/reteco-v1.1/track1_tempo/$domain"
done
```

For a single domain such as politics, substitute `domain=politics` and execute the Java command above with `-input collections/track1_tempo/politics -index indexes/reteco-v1.1/track1_tempo/politics.building`. This is the real indexing method, not a placeholder for the flags. The stock Jackson 20-million-character limit can silently produce an incomplete HSM index despite a zero exit code; always check counts and segments before renaming.

BM25 `k1=0.9`, `b=0.4` are **search-time** parameters. For Track 1a comparisons to RETECO’s official gensim BM25 baseline, use Anserini `SearchCollection -bm25.querySide -bm25.k1 0.9 -bm25.b 0.4 -hits 1000` (close but not identical). RETECO’s official metric is nDCG@10, based on its version-matched qrels.

Source text: **CC BY-SA 4.0** (retain upstream Stack Exchange attribution and share-alike); task annotations: **CC BY 4.0**. Cite the [dataset and attribution](https://huggingface.co/datasets/DataScience-UIBK/RETECO-SemEval2027) when using these indexes.

## Original source

- [Original documentation](https://huggingface.co/datasets/castorini/prebuilt-indexes-reteco/blob/1cdd540ec654a00dbc2034c199ea018ed6ce492e/lucene-inverted/tf/lucene-inverted.reteco-v1.1-track1.20261017.1.6.0.README.md)
