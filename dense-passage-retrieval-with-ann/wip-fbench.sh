#!/bin/sh

clients=${1:-10}
vespa-fbench -P -n $clients -c 1 -z -q fbench-queries -H "Content-Type: application/json" localhost 8080
