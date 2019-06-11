#!/bin/bash

git clone https://github.com/HaywardPeirce/family-tree.git
cd family-tree
git checkout example
git pull

cd ..
git clone https://github.com/HaywardPeirce/gedcom2html.git
cd gedcom2html
git checkout python3
git pull

wget https://d3js.org/d3.v4.min.js -nc -P assets/js/

python example.py