start_app:
	docker-compose up

build_app:
	docker-compose build

stop_app:
	@eval docker stop $$(docker ps -a -q)
	docker-compose down

ssh_logstash:
	docker exec -it logstash bash

ssh_django_web:
	docker exec -it django_web bash

ssh_db:
	docker exec -it db bash

ssh_es:
	docker exec -it es bash

ssh_kibana:
	docker exec -it kibana bash