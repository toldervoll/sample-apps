#!/bin/sh

clients=${1:-1}
if test "$clients" eq 1
then
  timeout=-1
else
  timeout=20
fi
vespa-fbench -P -n $clients -c 0 -z -r 0 -s $timeout -p 20 -q fbench-queries2 -H "Content-Type: application/json" localhost 8080
