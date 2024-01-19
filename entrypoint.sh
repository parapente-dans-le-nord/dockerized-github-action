#!/bin/sh -l

echo "tous les params :"
echo $@

echo "Github_output = $GITHUB_OUTPUT"

echo "current dir = $PWD"

echo "liste des fichier : "
ls -larth

GREETING=$(python myscript.py $INPUT_WHO_TO_GREET)

echo "greeting=$GREETING" >> "$GITHUB_OUTPUT"

exit 0
