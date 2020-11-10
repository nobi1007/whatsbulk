#!/bin/bash

echo '\n---- installing python3 ----\n'
brew install python3

echo '\n---- creating virtualenv and activating it----\n'
virtualenv whatsbulk-venv && source whatsbulk-venv/bin/activate

echo '\n---- installing dependencies ----\n'
python3 install -r requirements.txt

echo '\n---- Success, now you can run start.sh ----\n'