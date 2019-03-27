import attr

from model.ManagerStatus import MyManagerStatus
from model.ProgUnderTestStatus import ProgUnderTestStatus
from service.ExternalApi import ExternalApi


@attr.s
class ExternalApiService(ExternalApi):

    def __init__(self):
        super().__init__()
        self.status = MyManagerStatus()

    def run(self, command):
        # todo get the correct ProgUnderTestStatus according to the command.role
        status = ProgUnderTestStatus()
        self.status.add(status)
        # todo run the program under test
        status.command(command['action'])
        return self.status

    def pause(self, role):
        return {
            'role': role,
            'command': 'pause'}

    def restart(self, role):
        return {
            'role': role,
            'command': 'restart'}

    def stop(self, role):
        return {
            'role': role,
            'command': 'stop'}

