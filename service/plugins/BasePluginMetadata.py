from abc import ABCMeta, abstractmethod


class BasePluginMetadata(metaclass=ABCMeta):


    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def generator(self):
        pass

    @abstractmethod
    def logAnalyzer(self):
        pass

    @abstractmethod
    def statsAnalyzer(self):
        pass

    @abstractmethod
    def crashAnalyzer(self):
        pass

    @abstractmethod
    def additionalInfo(self):
        pass

    @abstractmethod
    def driver(self):
        pass

    @abstractmethod
    def swagger(self):
        pass
