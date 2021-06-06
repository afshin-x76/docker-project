#!/bin/sh

python manage.py migrate
python manage.py addsuppliergroup
python manage.py addsuperuser
gunicorn ShopProject.wsgi:application --workers=3 --env DJANGO_SETTINGS_MODULE=ShopProject.settings.local --bind 0.0.0.0:8001
# gunicorn ShopProject.wsgi:application --workers=3 --timeout 0 --env DJANGO_SETTINGS_MODULE=ShopProject.settings.local --bind=unix:/team-A/ShopProject/gunicorn.sock


