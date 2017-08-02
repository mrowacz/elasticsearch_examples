#!/bin/bash

docker run -d --name elastic_instance -p 9200:9200 -e "http.host=0.0.0.0" -e "transport.host=127.0.0.1" docker.elastic.co/elasticsearch/elasticsearch:5.5.1
docker run --link elastic_instance:elasticsearch -p 5601:5601 -d docker.elastic.co/kibana/kibana:5.5.1

