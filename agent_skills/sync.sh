#!/bin/bash
set -e

if [ $# -ne 1 ]; then
    echo "Usage: $0 <source-directory>"
    exit 1
fi

rsync -av --progress "$1" ./
