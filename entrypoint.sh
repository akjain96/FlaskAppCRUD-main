#!/usr/bin/env bash

echo "MySQL Database started!"

flask db init
flask db migrate
flask db upgrade
cd /Flask-Crud
python app.py