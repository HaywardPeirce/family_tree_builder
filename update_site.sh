#!/bin/bash

git clone https://github.com/HaywardPeirce/family-tree.git
cd family-tree
git checkout $REPO_BRANCH_FAMILY_TREE
git pull
git fetch --all
git reset --hard origin/master

cd ..
git clone https://github.com/HaywardPeirce/gedcom2html.git
cd gedcom2html
git checkout $REPO_BRANCH_P2G
git pull
git fetch --all
git reset --hard origin/python3

wget https://d3js.org/d3.v4.min.js -nc -P assets/js/

python generate.py -f ../family-tree/family.ged -t 'Family Tree'

cd ..
cp -R family-tree/resources gedcom2html/generated/resources

npm config set prefix ~/.local

npm install -g firebase-tools

firebase deploy --token "$FIREBASE_TOKEN"