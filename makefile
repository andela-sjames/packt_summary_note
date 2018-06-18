start_app:
	docker-compose up

build_app:
	docker-compose build

stop_app:
	@eval docker stop $$(docker ps -a -q)
	docker-compose down

ssh_logstash:
	docker exec -it noteapp_logstash bash

ssh_django_web:
	docker exec -it noteapp_django_web bash

ssh_db:
	docker exec -it noteapp_db bash

ssh_es:
	docker exec -it noteapp_es bash

ssh_kibana:
	docker exec -it noteapp_kibana bash

ssh_filebeat:
	docker exec -it noteapp_filebeat bash

# run this after all services has started from the root folder
load_beat_template:
	docker-compose run --rm filebeat curl -H 'Content-Type: application/json' -XPUT 'http://es:9200/_template/filebeat' -d@filebeat.template.json
