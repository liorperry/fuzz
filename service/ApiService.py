from service import modules
from service.LifeCycleApi import LifeCycleApi


class ExternalApiService(LifeCycleApi):

    def __init__(self):
        super().__init__()

    def run(self, name: str = 'all'):
        statuses = dict()
        if name == 'all':
            for key, value in modules.items():
                statuses[key] = value.driver.run(name)
        else:
            module = modules[name]
            statuses[name] = module.driver().run(name)

        return statuses

    # pause all
    def pause(self, name: str = 'all'):
        statuses = dict()
        if name == 'all':
            for key, value in modules.items():
                statuses[key] = value.driver().pause(name)
        else:
            module = modules[name]
            statuses[name] = module.driver().pause(name)

        return statuses

    # restart all
    def restart(self, name: str = 'all'):
        statuses = dict()
        if name == 'all':
            for key, value in modules.items():
                statuses[key] = value.driver().restart(name)
        else:
            module = modules[name]
            statuses[name] = module.driver().restart(name)

        return statuses

    # stop all
    def stop(self, name: str = 'all'):
        statuses = dict()
        if name == 'all':
            for key, value in modules.items():
                statuses[key] = value.driver().stop(name)
        else:
            module = modules[name]
            statuses[name] = module.driver().stop(name)

        return statuses
