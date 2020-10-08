#!/bin/bash

pip3 install nuitka
pip3 install hashlib
clear
nuitka3 src/src.py
rm -rf src.build
mv src.bin pass_man
rm -rf src/
rm build_script.sh
rm README.md
rm build_script_alternate.sh
clear
echo "build completed"
