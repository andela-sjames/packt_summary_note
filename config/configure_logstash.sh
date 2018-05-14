chown -R logstash:root /etc/logstash/conf.d
chmod 0750 /etc/logstash/conf.d
chmod 0640 /etc/logstash/conf.d/*

logstash -f /etc/logstash/conf.d/logstash.conf
bin/logstash-plugin install logstash-filter-translate
