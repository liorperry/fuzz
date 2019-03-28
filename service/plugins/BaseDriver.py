import asyncio
from abc import abstractmethod

from model.Status import Status
from service.LifeCycleApi import LifeCycleApi


class baseDriver(LifeCycleApi):

    def __init__(self, args, generator):
        self.generator = generator
        self.init(args)

    def run(self, name):
        self.start()
        return Status.RUNNING

    def pause(self, name):
        # todo call stop
        return Status.STOPPED

    def restart(self, name):
        self.start()
        return Status.RUNNING

    def stop(self, name):
        # todo call stop
        return Status.STOPPED

    @abstractmethod
    def init(self, args):
        pass

    def runGenerator(self):
        self.generator.generate()

    @abstractmethod
    async def runFuzzer(self):
        pass

    def start(self):
        # run generator to create input files
        self.runGenerator()
        # run fuzzer based on the generated input files
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
        asyncio.run(self.runFuzzer())
