#!/bin/bash

# start django
python manage.py makemigrations
python manage.py migrate

# create admin superuser, build es index and run server
echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'nimda')" | python manage.py shell
# python manage.py search_index --rebuild (use this to delete and rebuild index)

# wait for elasticsearch status to be green
function es_ready() {
    curl -o -XGET 'http://es:9200/_cluster/health?wait_for_status=green&pretty=true'
}

until es_ready; do
  >&2 echo "elasticsearch is unavailable - sleeping"
  sleep 5
done

# Start app
>&2 echo "elasticsearch is up - executing command"

# auto generate data for database
python manage.py loadtestdata summary.SummaryNote:5

python manage.py runserver 0.0.0.0:8000
