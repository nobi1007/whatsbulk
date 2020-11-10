#!/bin/bash

echo '1. ---- installing python3 ----'
brew install python3

echo '2. ---- creating virtualenv and activating it----'
virtualenv whatsbulk-venv 
source whatsbulk-venv/bin/activate

echo '3. ---- installing dependencies ----'
pip install -r requirements.txt

echo '4. ---- Success, now you can run start.sh ----'