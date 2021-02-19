#!/bin/sh

python3 ./bin/wip-make-fbench-queries.py NQ-open.dev.jsonl dense
sed -i -e 's/}$/, "tracelevel": 3 }/' fbench-queries
rm -f fbench-queries.out
vespa-fbench -P -n 1 -c 1 -z -r 0 -s -1 -p 20 -q fbench-queries -H "Content-Type: application/json" -o fbench-queries.out localhost 8080
 
sed -n -e 's/.*\\"query_embedding\\":\[tensor<float>(x\[769\]):\(\[[^]]*\]\)\].*/\1/p' < fbench-queries.out > query-embeddings.txt
