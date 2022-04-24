#!/bin/bash

declare -a services=("garden")

for SERVICE in "${services[@]}"; do
    DESTDIR="./pkgs/${SERVICE}"
    cd $DESTDIR
    poetry build
done