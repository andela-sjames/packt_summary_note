#!/bin/bash

# start django
python manage.py makemigrations
python manage.py migrate

# create admin superuser, build es index and run server
echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'nimda')" | python manage.py shell
python manage.py search_index --rebuild
python manage.py runserver 0.0.0.0:8000
