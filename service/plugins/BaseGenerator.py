import getopt
from abc import ABCMeta, abstractmethod

from service.plugins.sqlite.randQuery import Randomize


class BaseGenerator(metaclass=ABCMeta):
    def __init__(self, args):
        self.output_dir = ''
        self.init_parse(args)
        self.randPkg = Randomize()
        self.max_file_lines = 50

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def init_parse(self):
        pass
