#!/bin/bash

# load variables from .env file
while read -r line; do [[ -n "${line}" ]] && eval 'export ${line}'; done < .env

alembic upgrade head
python app.py

# unset variables from .env file
while read -r line; do [[ -n "${line}" ]] && unset "$(echo "${line}" | awk -F= '{print $1}')"; done < .env
