#!/bin/bash
# Install dependencies
pip install -r requirements.txt

# Collect static files
python mycollection/manage.py collectstatic --noinput
