import json
import uuid

from model.ManagerStatus import Status


class ProgUnderTestStatus:
    def __init__(self, command):
        self.status = Status.NOT_INITIATED
        self.id = uuid.uuid4().hex
        self.command = command

    def id(self):
        return self.id

    def status(self):
        return self.status

    def command(self):
        return self.command

    def toJSON(self):
        return json.dumps({'status': self.status, 'id': self.id, 'command': self.command})


