import abc


class ExternalApi(abc.ABC):
    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def pause(self):
        pass

    @abc.abstractmethod
    def restart(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass
