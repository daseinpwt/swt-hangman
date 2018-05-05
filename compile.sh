#!/bin/bash
set -e
rm -rf ./dist
rm -rf ./src/recorder/reports/*.txt
pyinstaller --clean --distpath ./dist --onefile --name hangman hangman.spec
rm -rf ./build
