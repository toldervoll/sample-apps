#!/bin/sh

clients=${1:-1}
suffix=$2
timeout=60
vespa-fbench -P -n $clients -c 0 -z -r 0 -s $timeout -p 20 -q fbench-queries2${suffix:+-}$suffix -H "Content-Type: application/json" localhost 8080
