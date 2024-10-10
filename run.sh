#!/bin/sh

export FLASK_APP=./main.py

python -m flask --debug run -h 0.0.0.0
