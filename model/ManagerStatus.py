import json
import uuid

from model.Status import Status


# Status manager for the entire client
from service.utils import MyEncoder


class MyManagerStatus:
    def __init__(self):
        self.clientStatus = Status.NOT_INITIATED
        self.id = uuid.uuid4().hex
        self.progs = dict()

    def toJSON(self):
        return json.dumps({'status': self.clientStatus, 'id': self.id, 'progs': self.progs}, cls=MyEncoder)

    def add(self, prog):
        self.progs[prog.name()] = prog

    def progs(self):
        return self.progs

    def prog(self, name):
        return self.progs[name]

    def status(self, name):
        return self.progs[name]

    def updateStatus(self):
        # print("... scanning ...")
        return
