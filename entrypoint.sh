#!/bin/sh -l

echo "tous les params :"
echo $@

echo "Github_output = $GITHUB_OUTPUT"

GREETING=$(python myscript.py $INPUT_WHO_TO_GREET)

echo "greeting=$GREETING" >> "$GITHUB_OUTPUT"

exit 0
