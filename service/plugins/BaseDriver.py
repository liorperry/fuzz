import asyncio
import os
import uuid
from abc import abstractmethod
from concurrent.futures.thread import ThreadPoolExecutor

from model.Status import Status
from service.LifeCycleApi import LifeCycleApi


class baseDriver(LifeCycleApi):

    def __init__(self, args, generator, metadata, managerStatus):
        self.managerStatus = managerStatus
        self.metadata = metadata
        self.generator = generator
        self.init(args)
        self.output_dir = args['output_dir']
        self.executor = ThreadPoolExecutor(max_workers=10)

    def run(self, command):
        state = self.start(command)
        # update status state with the manager
        self.managerStatus.status(command.getRole()).set_status(state)
        return state

    def pause(self, command):
        # todo call stop
        return Status.STOPPED

    def restart(self, command):
        if self.stop(command) == Status.STOPPED:
            return self.start(command)

    def stop(self, command):
        # todo call stop
        return Status.STOPPED

    @abstractmethod
    def init(self, args):
        pass

    def runGenerator(self, runId, command):
        self.generator.generate(runId, command)

    @abstractmethod
    async def runFuzzer(self, runId, command):
        pass

    @abstractmethod
    def name(self):
        pass

    def start(self, command):
        runId = uuid.uuid4().hex
        # run generator to create input files
        concurrency = command.getConcurrency()
        for i in range(0, concurrency):
            print('submit {} for role {}'.format(i, command.getRole()))
            self.executor.submit(self.execute, runId, command)
        return Status.RUNNING

    # run in concurrency
    def execute(self, runId, command):
        self.currentDir = os.path.dirname(os.path.realpath(__file__))
        self.runDir = os.path.join(self.currentDir + '/' + self.metadata.name() + '/' + self.output_dir + '/' + runId)
        if not os.path.exists(self.runDir):
            os.makedirs(self.runDir)

        # run generator to create input files
        self.runGenerator(runId, command)
        # run fuzzer based on the generated input files
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
        asyncio.run(self.runFuzzer(runId, command))
