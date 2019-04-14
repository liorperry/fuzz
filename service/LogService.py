import json

from elasticsearch import Elasticsearch

from service.utils import MyEncoder

LOG_INDEX = 'log-index'


class LogService:
    def __init__(self) -> None:
        # by default we connect to localhost:9200
        self.es = Elasticsearch()
        # create an index in elasticsearch, ignore status code 400 (index already exists)
        self.es.indices.create(index=LOG_INDEX, ignore=400)

    def report(self, logEvent):
        dump = json.dumps(logEvent, cls=MyEncoder)
        self.es.index(index=LOG_INDEX, id=logEvent.id, body=dump)
