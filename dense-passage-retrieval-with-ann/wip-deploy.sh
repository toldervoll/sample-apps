#!/bin/sh

export VESPA_USER=$(id -un)
export VESPA_HOME=$HOME/vespa
export VESPA_CONFIGSERVERS=$(hostname)

if ! test -f src/main/application/files/reader.onnx
then
    ./wip-export-model.sh
fi
if ! test -f src/main/application/files/reader.onnx
then
    echo Failed to export model, reader
    exit 1
fi
if ! test -f src/main/application/files/question_encoder.onnx
then
    echo Failed to export model, question encoder
    exit 1
fi
if ! mvn clean package
then
    echo Failed to package application
    exit 1
fi

vespa-deploy prepare target/application.zip && vespa-deploy activate
