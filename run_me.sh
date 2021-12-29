#!/bin/bash

python src/main.py
flake8 src/
coverage run --source src/ -m pytest && coverage report -m
