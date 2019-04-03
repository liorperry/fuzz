
import abc


class LifeCycleApi(abc.ABC):
    @abc.abstractmethod
    def run(self, command):
        pass

    @abc.abstractmethod
    def pause(self, command):
        pass

    @abc.abstractmethod
    def restart(self, command):
        pass

    @abc.abstractmethod
    def stop(self, command):
        pass
