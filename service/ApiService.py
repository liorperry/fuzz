import attr

from model.ManagerStatus import MyManagerStatus
from service.ExternalApi import ExternalApi


@attr.s
class ExternalApiService(ExternalApi):

    def __init__(self):
        super().__init__()
        self.status = None

    def run(self):
        self.status = MyManagerStatus()
        return self.status

    def pause(self):
        return {'command': 'pause'}

    def restart(self):
        return {'command': 'restart'}

    def stop(self):
        return {'command': 'stop'}

