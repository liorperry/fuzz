from enum import Enum

import attr


@attr.s
class ProgUnderTestStatus:
    def __init__(self) -> None:
        super().__init__()
        self.status = Status.NOT_INITIATED


class Status(Enum):
    NOT_INITIATED = 1
    INITIATED = 2
    RUNNING = 3
    PASSED = 3
