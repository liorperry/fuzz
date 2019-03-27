import asyncio
from abc import ABCMeta, abstractmethod


class baseDriver(metaclass=ABCMeta):

    def __init__(self, args):
        self.init(args)

    @abstractmethod
    def init(self, args):
        pass

    def start(self):
        asyncio.set_event_loop_policy(
            asyncio.WindowsProactorEventLoopPolicy())
        asyncio.run(self.runGenerator())

    @abstractmethod
    async def runGenerator(self):
        pass
