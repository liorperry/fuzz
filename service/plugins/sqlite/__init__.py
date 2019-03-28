# File: sqlitePluginMetadata
import os

from service.plugins.BasePluginMetadata import BasePluginMetadata
from service.plugins.sqlite.driver import Driver
from service.plugins.sqlite.generator import Generator

class sqlitePluginMetadata(BasePluginMetadata):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'sqlight'
        # -i sqlite_cmd.sql - o data.csv --target-path =..\sqlite327\sqlite3.exe
        args = dict()
        args['output_file'] = 'sqlite_cmd.sql'
        args['input_file'] = 'data.csv'
        args['sqlite_path'] = '..\lib\sqlite3.exe'
        args['output_dir'] = '../target'
        args['template_dir'] = os.getcwd()

        self.generator = Generator(args)
        self.driver = Driver(args, self.generator)

    def name(self):
        return self.name

    def command(self):
        return 'sqlite_cmd.sql -o data.csv --target-path=..\sqlite327\sqlite3.exe'

    def generator(self):
        return Generator()

    def logAnalyzer(self):
        return 'logAnalyzer.class.name'

    def statsAnalyzer(self):
        return 'statsAnalyzer.class.name'

    def crashAnalyzer(self):
        return 'crashAnalyzer.class.name'

    def additionalInfo(self):
        return 'additionalInfo'

    def swagger(self):
        return 'sqlite_swagger.json'

    def toJson(self):
        return {
            'name': self.name(),
            'cmd': self.command(),
            'swagger': self.swagger()
        }

    def driver(self):
        return self.driver
