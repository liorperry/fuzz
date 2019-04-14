import json


class Command:
    def __init__(self, role, command, details = None, concurrency: int=10, timeout: int=60*3, ) -> None:
        super().__init__()
        self._role = role
        self._command = command
        self._concurrency = concurrency
        self._timeout = timeout
        self._details = details

    def role(self, role):
        self._role = role

    def getRole(self):
        return self._role

    def concurrency(self, concurrency):
        self._concurrency = concurrency

    def getConcurrency(self):
        return self._concurrency

    def command(self, command):
        self._command = command

    def getCommand(self):
        return self._command

    def timeout(self, timeout):
        self._timeout = timeout

    def getTimeout(self):
        return self._timeout

    def details(self, details):
        self._details = details

    def getDetails(self):
        return self._details

    def toJSON(self):
        return self.__dict__

    # f = JSONDecoder(object_hook = fromJson).decode('{"role": "myRole", "concurrency" : "100", "timeout": 10000 }')
    def fromJson(json_object):
        return Command(json_object['role'],json_object['command'], json_object['concurrency'], json_object['timeout'], json_object['details'])