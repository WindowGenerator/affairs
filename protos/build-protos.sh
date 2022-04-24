#!/bin/bash

declare -a services=("garden")

for SERVICE in "${services[@]}"; do
    DESTDIR="./pkgs/${SERVICE}/garden_api"
    mkdir -p $DESTDIR
    poetry run python -m grpc_tools.protoc \
        --proto_path=$SERVICE \
        --python_out=$DESTDIR \
        --grpc_python_out=$DESTDIR \
        $SERVICE/*.proto
done