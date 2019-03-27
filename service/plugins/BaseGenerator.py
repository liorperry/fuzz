import getopt
from abc import ABCMeta, abstractmethod

from service.plugins.sqlite.randQuery import Randomize


class BaseGenerator(metaclass=ABCMeta):
    def __init__(self, args):
        self.output_dir = ''
        self.init_parse(args)
        self.randPkg = Randomize()
        self.max_file_lines = 50

    def init_parse(self, args):
        try:
            options, remainder = getopt.getopt(args, '', ['output-dir='])
        except getopt.GetoptError as err:
            print(err)
        for opt, arg in options:
            if opt in ('--output-dir'):
                self.output_dir = arg + '/'

    @abstractmethod
    def generate(self):
        pass
