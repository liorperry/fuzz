import json
import uuid
from enum import Enum


class MyManagerStatus:

    def __init__(self):
        self.status = Status.NOT_INITIATED
        self.id = uuid.uuid4().hex

    def __repr__(self):
        return {
            'id': self.id,
            'status': self.status
        }

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)


class Status(Enum):
    NOT_INITIATED = 1
    INITIATED = 2
    RUNNING = 3
    PASSED = 3
