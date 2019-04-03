import asyncio
import os
import uuid
from abc import abstractmethod

from model.Status import Status
from service.LifeCycleApi import LifeCycleApi


class baseDriver(LifeCycleApi):

    def __init__(self, args, generator, metadata):
        self.metadata = metadata
        self.generator = generator
        self.init(args)
        self.output_dir = args['output_dir']

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

    def runGenerator(self, runId):
        self.generator.generate(runId)

    @abstractmethod
    async def runFuzzer(self, runId):
        pass

    @abstractmethod
    def name(self):
        pass

    def start(self, command):
        runId = uuid.uuid4().hex
        # run generator to create input files
        self.execute(runId)

    def execute(self, runId):
        self.currentDir = os.path.dirname(os.path.realpath(__file__))
        self.runDir = os.path.join(self.currentDir +'/'+self.metadata.name+'/'+ self.output_dir + '/' + runId)
        if not os.path.exists(self.runDir):
            os.makedirs(self.runDir)

        # run generator to create input files
        self.runGenerator(runId)
        # run fuzzer based on the generated input files
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
        asyncio.run(self.runFuzzer(runId))

