import json

from elasticsearch import Elasticsearch

from service.utils import MyEncoder
from setup import ES_LOG_INDEX


class LogService:
    def __init__(self) -> None:
        # by default we connect to localhost:9200
        self.es = None

    def init(self):
        from setup import ES_HOST, ES_LOG_INDEX
        self.es = Elasticsearch(ES_HOST)
        # create an index in elasticsearch, ignore status code 400 (index already exists)
        self.es.indices.create(index=ES_LOG_INDEX, ignore=400)

    def report(self, logEvent):
        dump = json.dumps(logEvent, cls=MyEncoder)
        self.es.index(index=ES_LOG_INDEX, id=logEvent.id, body=dump)
