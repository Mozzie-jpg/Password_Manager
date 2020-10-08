#!/bin/bash

pip3 install nuitka
pip3 install hashlib
clear
echo "building into binary..."
nuitka3 src/src.py
rm -rf src.build
mv src.bin pass_man
clear
echo "build completed"
