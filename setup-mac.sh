#!/bin/bash

echo -e ' \n ---- Installing python3.9 ---- \n'
brew install python3

echo -e '\n ---- Creating virtualenv and activating it ---- \n'
virtualenv whatsbulk-venv 
source ./whatsbulk-venv/bin/activate

echo -e '\n ---- Installing dependencies ----\n'
pip install -r ./requirements.txt

echo -e '\n ---- Success, now you can run start.sh ----\n'