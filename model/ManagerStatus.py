import attr
from enum import Enum


@attr.s
class ManagerStatus:
    def __init__(self) -> None:
        super().__init__()
        self.status = Status.NOT_INITIATED


class Status(Enum):
    NOT_INITIATED = 1
    INITIATED = 2
    RUNNING = 3
    PASSED = 3
