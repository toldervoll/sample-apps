#!/bin/sh

clients=${1:-1}
vespa-fbench -P -n $clients -c 1 -z -r 0 -s -1 -p 20 -q fbench-queries2 -H "Content-Type: application/json" localhost 8080
