from elasticsearch import Elasticsearch
from datetime import datetime

import os
import time

# you can use RFC-1738 to specify the url
es = Elasticsearch(['http://elastic:changeme@localhost:9200'])
es.indices.create(index='load', ignore=[400, 401])

while True:
    ov = os.getloadavg()
    es.index(index="load", doc_type="value", body = {
        "load" : ov[0],
        "timestamp" : datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        })
    time.sleep(60)

