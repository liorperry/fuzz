import json

from model.Status import Status


class ProgUnderTestStatus:
    def __init__(self, details):
        self.status = Status.NOT_INITIATED
        self.details = details
        self.instancesRunning: int = 0
        self.instancesCompleted: int = 0

    def id(self):
        return self.id

    def status(self):
        return self.status

    def set_status(self, status):
        self.status = status
        return self.status

    def details(self):
        return self.details

    def instances(self):
        return self.instances

    def running(self):
        return self.instancesRunning

    def completed(self):
        return self.instancesCompleted

    def toJSON(self):
        return json.dumps({'status': self.status, 'id': self.id, 'command': self.command})
