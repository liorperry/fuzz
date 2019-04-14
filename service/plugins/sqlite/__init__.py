# File: sqlitePluginMetadata
import os

from service.plugins.BasePluginMetadata import BasePluginMetadata
from service.plugins.sqlite.driver import Driver
from service.plugins.sqlite.generator import Generator


class sqlitePluginMetadata(BasePluginMetadata):

    def _init(self, managerStatus, logService):
        self._name = 'sqlite'
        # -i sqlite_cmd.sql - o data.csv --target-path =..\sqlite327\sqlite3.exe
        self._args = dict()
        self._args['output_file'] = 'sqlite_cmd.sql'
        self._args['input_file'] = 'data.csv'
        self._args['log_file'] = 'log_'
        self._args['sqlite_path'] = '/lib/sqlite3.exe'
        self._args['output_dir'] = '/target'
        self._args['template_dir'] = os.getcwd()

        self._managerStatus = managerStatus
        self._generator = Generator(self._args, self, logService)
        # init sqlite driver
        self._driver = Driver(self._args, self._generator, self, managerStatus, logService)


    def args(self):
        return self._args

    def name(self):
        return self._name

    def generator(self):
        return self._generator

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
            'name': self._name,
            'swagger': self.swagger
        }

    def driver(self):
        return self._driver
