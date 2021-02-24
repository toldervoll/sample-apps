#!/bin/sh

clients=${1:-1}
suffix=$2
if test "$clients" -eq 1
then
  timeout=-1
else
  timeout=60
fi
vespa-fbench -P -n $clients -c 0 -z -r 0 -s $timeout -p 20 -q fbench-queries2${suffix:+-}$suffix -H "Content-Type: application/json" localhost 8080
