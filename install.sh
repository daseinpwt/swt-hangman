#!/bin/bash
set -e

if ! hash python; then
    echo "Error: python is not installed"
    exit 1
fi

ver=$(python -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')
if [ "$ver" -lt "36" ]; then
    echo "Error: this script requires python 3.6 or greater"
    exit 1
fi

if ! hash pyinstaller; then
    echo "Error: pyinstaller is not installed"
    exit 1
fi

. ./compile.sh
cp ./dist/hangman /usr/local/bin

echo ""
echo "Installation complete. Enjoy!"
