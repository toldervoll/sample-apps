#!/bin/sh

# Shortcut version of exporting to onnx model by just decompressing
# compressed files.

# $ python3 ./bin/export-reader-model.py src/main/application/files/reader.onnx
# $ python3 ./bin/export-query-model.py src/main/application/files/question_encoder.onnx

FILES=src/main/application/files
mkdir -p $FILES
zstd -df ~/DPR/model/reader.onnx.zst -o $FILES/reader.onnx
zstd -df ~/DPR/model/question_encoder.onnx.zst -o $FILES/question_encoder.onnx

echo Note, use 7-SNAPSHOT as vespa_version in pom.xml
