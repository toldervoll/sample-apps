#!/bin/sh

sed -n -e 's/.*"text_embedding": {"values": \(\[[^]]*\]\).*/\1/p' < feed0 > text-embeddings.txt
