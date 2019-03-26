import json


class RunCommand:
    def __init__(self, role=None, concurrency=10, timeout=60*3) -> None:
        super().__init__()
        self.role = role
        self.concurrency = concurrency
        self.timeout = timeout

    def role(self, role):
        self.role = role

    def concurrency(self, concurrency):
        self.concurrency = concurrency

    def timeout(self, timeout):
        self.timeout = timeout

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)

    # f = JSONDecoder(object_hook = fromJson).decode('{"role": "myRole", "concurrency" : "100", "timeout": 10000 }')
    def fromJson(json_object):
        if 'fname' in json_object:
            return RunCommand(json_object['role'],json_object['concurrency'],json_object['timeout'])