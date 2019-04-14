# File: sqlitePluginMetadata
import os

from service.plugins.BasePluginMetadata import BasePluginMetadata
from service.plugins.crash.driver import Driver
from service.plugins.crash.generator import Generator


class crashPluginMetadata(BasePluginMetadata):

    def _init(self, managerStatus,logService):
        self._name = 'crash'
        self._args = dict()
        self._args['output_file'] = ''
        self._args['input_file'] = ''
        self._args['log_file'] = 'log_'
        self._args['crash_path'] = '/lib/crash.exe'
        self._args['output_dir'] = '/target'
        self._args['crash_dir'] = 'C:\Windows\System32\config\systemprofile\AppData\Local\CrashDumps'
        self._args['template_dir'] = os.getcwd()

        self._managerStatus = managerStatus
        self._generator = Generator(self._args, self, logService)
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
        return 'crash_swagger.json'

    def toJson(self):
        return {
            'name': self._name,
            'swagger': self.swagger
        }

    def driver(self):
        return self._driver
