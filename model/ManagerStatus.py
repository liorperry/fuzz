import json
import uuid

from model import ProgUnderTestStatus
from model.Status import Status


class MyManagerStatus:
    def __init__(self):
        self.status = Status.NOT_INITIATED
        self.id = uuid.uuid4().hex
        self.progs = dict()

    def toJSON(self):
        return json.dumps({'status': self.status, 'id': self.id})

    def add(self, prog: ProgUnderTestStatus):
        self.progs[prog.id()] = prog

    def progs(self):
        return self.progs

    def prog(self, name):
        return self.progs[name]

    def status(self, name):
        return self.progs[name]

    def progStatus(self, id):
        return self.progs[id]


