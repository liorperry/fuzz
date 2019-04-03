import json
import uuid

from model import ProgUnderTestStatus
from model.Status import Status


# Status manager for the entire client
class MyManagerStatus:
    def __init__(self):
        self.clientStatus = Status.NOT_INITIATED
        self.id = uuid.uuid4().hex
        self.progs = dict()

    def toJSON(self):
        return json.dumps({'status': self.clientStatus, 'id': self.id})

    def add(self, prog: ProgUnderTestStatus):
        self.progs[prog.id()] = prog

    def progs(self):
        return self.progs

    def prog(self, name):
        return self.progs[name]

    def status(self, name):
        return self.progs[name]


