from service.plugins import BasePluginMetadata


class SqlightPluginMetadata(BasePluginMetadata):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'sqlight'

    def name(self):
        return self.name

    def generator(self):
        return 'generator.class.name'

    def logAnalyzer(self):
        return 'logAnalyzer.class.name'

    def statsAnalyzer(self):
        return 'statsAnalyzer.class.name'

    def crashAnalyzer(self):
        return 'crashAnalyzer.class.name'

    def additionalInfo(self):
        return 'additionalInfo'
