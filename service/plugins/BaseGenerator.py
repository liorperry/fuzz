from abc import ABCMeta, abstractmethod


class BaseGenerator(metaclass=ABCMeta):
    def __init__(self, args, metadata):
        self.metadata = metadata
        self.output_dir = ''
        self.init_parse(args)

    @abstractmethod
    def generate(self, runId, command, completeHook):
        pass

    @abstractmethod
    def init_parse(self):
        pass

    # todo status end of run
    # #of lines
    # crash / not
    # execution time
    def completeHook(self, role, status):
        pass
