import asyncio
import os
import time
import uuid
from abc import abstractmethod
from concurrent.futures.thread import ThreadPoolExecutor

from model.Status import Status
from service.LifeCycleApi import LifeCycleApi
from service.plugins import DELAY


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
        progStatus = self.managerStatus.status(command.getRole())
        return progStatus.set_status(state).set_running(command.getConcurrency())

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

    def runGenerator(self, runId, command, completeHook):
        self.generator.generate(runId, command, completeHook)

    @abstractmethod
    async def runFuzzer(self, runId, command, completeHook):
        pass

    @abstractmethod
    def name(self):
        pass

    def completeHook(self, role, status):
        progStatus = self.managerStatus.status(role)
        if status == Status.PASSED:
            progStatus.incrementCompleted()
        if status == Status.ERROR:
            progStatus.incrementErrors()

    def start(self, command ):
        # run generator to create input files
        concurrency = command.getConcurrency()
        for i in range(0, concurrency):
            runId = uuid.uuid4().hex
            # print('submit {} for role {}'.format(i, command.getRole()))
            self.executor.submit(self.execute, runId, command, self.completeHook)
            # delay between executions
            time.sleep(DELAY)
        return Status.RUNNING

    # run in concurrency
    # handle timeout
    def execute(self, runId, command, completeHook):
        self.currentDir = os.path.dirname(os.path.realpath(__file__))
        self.runDir = os.path.join(self.currentDir + '/' + self.metadata.name() + '/' + self.output_dir + '/' + runId)
        if not os.path.exists(self.runDir):
            os.makedirs(self.runDir)

        # run generator to create input files
        self.runGenerator(runId, command, self.generator.completeHook)
        # run fuzzer based on the generated input files
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
        asyncio.run(self.runFuzzer(runId, command, completeHook))
