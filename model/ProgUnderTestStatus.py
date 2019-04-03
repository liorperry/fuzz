import json

from model.Status import Status


class ProgUnderTestStatus:
    def __init__(self, name, details):
        self._name = name
        self._status = Status.INITIATED
        self._details = details
        self._instancesRunning: int = 0
        self._instancesCompleted: int = 0

    def name(self):
        return self._name

    def status(self):
        return self._status

    def set_status(self, status):
        self._status = status
        return self._status

    def details(self):
        return self._details

    def instances(self):
        return self.instances

    def running(self):
        return self._instancesRunning

    def completed(self):
        return self._instancesCompleted

    def toJSON(self):
        return {'status': self._status, 'name': self._name,
                           'running': self._instancesRunning,
                           'completed': self._instancesCompleted,
                           'details': self._details}
