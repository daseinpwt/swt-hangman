#!/bin/bash
set -e
rm -rf ./dist
pyinstaller --clean --distpath ./dist --onefile --name hangman ./src/entry.py
rm -rf ./build
rm hangman.spec
