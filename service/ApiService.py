import attr

from service.ExternalApi import ExternalApi


@attr.s
class ExternalApiService(ExternalApi):

    def __init__(self):
        super().__init__()

    def run(self):
        return {'command': 'run'}

    def pause(self):
        return {'command': 'pause'}

    def restart(self):
        return {'command': 'restart'}

    def stop(self):
        return {'command': 'stop'}

