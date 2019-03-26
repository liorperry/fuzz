import attr
import uuid

from model import ManagerStatus
from service.ExternalApi import ExternalApi


@attr.s
class ExternalApiService(ExternalApi):

    def __init__(self):
        super().__init__()
        self.status = None

    def run(self):
        self.status = ManagerStatus(uuid.uuid5())
        return self.status

    def pause(self):
        return {'command': 'pause'}

    def restart(self):
        return {'command': 'restart'}

    def stop(self):
        return {'command': 'stop'}

