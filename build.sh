#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

cd task_api_project

python manage.py collectstatic --noinput
python manage.py migrate
