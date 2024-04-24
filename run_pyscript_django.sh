#!/usr/bin/env bash

python3 manage.py shell --command "$(cat $1)"

