#!/bin/sh

clients=${1:-10}
vespa-fbench -P -n $clients -c 1 -z -q fbench-queries2 -H "Content-Type: application/json" localhost 8080
