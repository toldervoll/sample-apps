#!/bin/sh

sed -n -e 's/^\(.*\)$/\/search\/\
{"yql": "select * from sources * where ([{\\"targetHits\\": 10, \\"hnsw.exploreAdditionalHits\\":1000}]nearestNeighbor(text_embedding, query_embedding));", "hits": 1, "ranking.features.query(query_embedding)": \1, "ranking.profile": "dense", "searchChain": "vespa"}/p' < query-embeddings.txt > fbench-queries2
