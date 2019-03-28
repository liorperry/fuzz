
import abc


class LifeCycleApi(abc.ABC):
    @abc.abstractmethod
    def run(self, name):
        pass

    @abc.abstractmethod
    def pause(self, name):
        pass

    @abc.abstractmethod
    def restart(self, name):
        pass

    @abc.abstractmethod
    def stop(self, name):
        pass
