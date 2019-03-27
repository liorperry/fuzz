from abc import ABCMeta, abstractmethod


class BasePluginMetadata(metaclass=ABCMeta, metaclass=ABCMeta, metaclass=ABCMeta, metaclass=ABCMeta, metaclass=ABCMeta,
                         metaclass=ABCMeta):
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