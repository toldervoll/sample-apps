#!/bin/sh

# Feed fragment

fragment=$1

COMPRESSED_FEED_DIR=$HOME/DPR/feed
COMPRESSED_FEED_FILE=$COMPRESSED_FEED_DIR/feed_$fragment.jsonl.zst

if test -f $COMPRESED_FEED_FILE
then
    echo Feeding $COMPRESSED_FEED_FILE
    zstdcat $COMPRESSED_FEED_FILE | java -jar $HOME/vespa/lib/jars/vespa-http-client-jar-with-dependencies.jar  --host localhost --port 8080
else
    echo Did not find feed file $COMPRESSED_FEED_FILE
    exit 1
fi
