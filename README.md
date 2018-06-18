# packt_summary_note
A simple summary note application using Python/Django to demonstrate the Elastic Stack for Packt Courseware

### Setup Using docker/docker-compose 

Before setting up this project, make sure you have docker installed on your system. 
[docker download page](https://www.docker.com/community-edition) 

If you have docker installed then continue the setup by cloning the project. 

Clone this repo using `git clone https://github.com/andela-sjames/packt_summary_note.git` 

From the root directory run `make build_app` to build each docker images for the respective services 

```
logstash
django_web
db
es
kibana
beats
``` 

The `makefile` has helper commands to start and stop the application as well as to ssh into the containers to see what's going on. 

To start the application run `make start_app` and to stop the application run `make stop_app`

To ensure that beats template is loaded when using beat(apparently)
use the command 

# run this after all services has started from the root folder
Reference: https://www.elastic.co/guide/en/beats/filebeat/5.4/config-filebeat-logstash.html
Reference: https://www.elastic.co/guide/en/beats/filebeat/5.4/filebeat-template.html#load-template-manually
```
make load_beat_template
```

**NB** 
When using docker with elasticsearch ensure that you have a minimum of 4GB assigned to memory as part of the computing resources assigned to docker.(advanced settings) 
