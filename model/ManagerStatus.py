import json
import uuid

from model import ProgUnderTestStatus


class MyManagerStatus:
    def __init__(self):
        self.status = Status.NOT_INITIATED
        self.id = uuid.uuid4().hex
        self.progs = dict()

    def toJSON(self):
        return json.dumps({'status': self.status, 'id': self.id})

    def add(self, prog: ProgUnderTestStatus):
        self.progs.a[prog.id()] = prog

    def progs(self):
        return self.progs

    def progStatus(self, id):
        return self.progs[id]



class Status:
    NOT_INITIATED = 'NOT_INITIATED'
    INITIATED = 'INITIATED'
    RUNNING = 'RUNNING'
    PASSED = 'PASSED'
