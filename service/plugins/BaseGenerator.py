import getopt
from abc import ABCMeta, abstractmethod

from service.plugins.sqlite.randQuery import Randomize


class BaseGenerator(metaclass=ABCMeta):
    def __init__(self, args, metadata):
        self.metadata = metadata
        self.output_dir = ''
        self.init_parse(args)
        self.randPkg = Randomize()

    @abstractmethod
    def generate(self, runId, command, completeHook):
        pass

    @abstractmethod
    def init_parse(self):
        pass

    def completeHook(self, role, status):
        pass
