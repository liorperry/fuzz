from abc import ABCMeta, abstractmethod

from model.ProgUnderTestStatus import ProgUnderTestStatus


class BasePluginMetadata(metaclass=ABCMeta):

    def __init__(self, managerStatus) -> None:
        self._init(managerStatus)
        # add progUnderTest status indication
        self._managerStatus.add(ProgUnderTestStatus(self.name(), self.args()))


    @abstractmethod
    def args(self):
        pass

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

    @abstractmethod
    def _init(self, managerStatus):
        pass
