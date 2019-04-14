from model.Status import Status


class ProgUnderTestStatus:
    def __init__(self, name, details):
        self._name = name
        self._status = Status.INITIATED
        self._details = details
        self._instancesRunning: int = 0
        self._instancesCompleted: int = 0
        self._instancesErrors: int = 0

    def set_status(self, status):
        self._status = status
        return self

    def set_running(self, running):
        self._instancesRunning = running
        return self

    def incrementCompleted(self):
        self._instancesCompleted += 1
        self._instancesRunning -= 1
        return self

    def incrementErrors(self):
        self._instancesErrors += 1
        self._instancesRunning -= 1
        return self

    def name(self):
        return self._name

    def status(self):
        return self._status

    def details(self):
        return self._details

    def instances(self):
        return self.instances

    def running(self):
        return self._instancesRunning

    def errors(self):
        return self._instancesErrors

    def completed(self):
        return self._instancesCompleted

    def toJSON(self):
        return self.__dict__
