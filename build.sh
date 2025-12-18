#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python task_api_project/manage.py collectstatic --noinput
python task_api_project/manage.py migrate
