#!/usr/bin/env bash

echo "MySQL Database started!!!!!!!!!!!!!"

flask db init
flask db migrate
flask db upgrade
echo "Hiiii"
cd /Flask-Crud
echo "Reached"
python app.py
echo "Reached!!!!!!!!!!"