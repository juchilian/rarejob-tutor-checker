#!/usr/bin/env bash

# For this issue https://github.com/docker/compose/issues/4076 (Probably)

PACKAGE=${1:-...}
ARGS=${2}

# find all files have 
testFiles=($(find . -name '*.py' -name 'test_*' | sed -e "s/\.\///"))

for file in ${testFiles[@]}
do
    echo "TEST: $file"
    python3 -B -m unittest -v $(echo $file)
    echo 
done