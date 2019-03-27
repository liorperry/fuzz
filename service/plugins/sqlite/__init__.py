# File: sqlitePluginMetadata
from service.plugins.sqlite.generator import Generator


class sqlitePluginMetadata():
    def __init__(self) -> None:
        super().__init__()
        self.name = 'sqlight'

    def name(self):
        return self.name

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

    def toJson(self):
        return {'details': 'details'}
