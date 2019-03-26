import attr
from enum import Enum


@attr.s
class ManagerStatus:
    def __init__(self, uuid) -> None:
        super().__init__()
        self.status = Status.NOT_INITIATED
        self.id = uuid

    def __repr__(self):
        return {
            'id': self.id,
            'status': self.status
        }


class Status(Enum):
    NOT_INITIATED = 1
    INITIATED = 2
    RUNNING = 3
    PASSED = 3
