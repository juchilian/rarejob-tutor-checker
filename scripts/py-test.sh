#!/usr/bin/env bash

# For this issue https://github.com/docker/compose/issues/4076 (Probably)

PACKAGE=${1:-...}
ARGS=${2}

# find all files have 
testFiles=($(find .  -type f -name '*.py' -name 'test_*'))

for file in ${testFiles[@]}
do
    echo $file
    python $(echo $file)
    echo
done