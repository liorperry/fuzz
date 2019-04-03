from service import pluginMgr
from service.LifeCycleApi import LifeCycleApi


class ExternalApiService(LifeCycleApi):

    def __init__(self):
        super().__init__()

    def run(self, command):
        statuses = dict()
        name: str = command.role
        if name == 'all':
            for key, value in pluginMgr.modules().items():
                statuses[key] = value.driver.run(name)
        else:
            module = pluginMgr.plugin(name)
            statuses[name] = module.driver().run(name)

        return statuses

    # pause all
    def pause(self, command):
        statuses = dict()
        name: str = command.role
        if name == 'all':
            for key, value in pluginMgr.modules().items():
                statuses[key] = value.driver.pause(name)
        else:
            module = pluginMgr.plugin(name)
            statuses[name] = module.driver().pause(name)

        return statuses

    # restart all
    def restart(self, command):
        statuses = dict()
        name: str = command.role
        if name == 'all':
            for key, value in pluginMgr.modules().items():
                statuses[key] = value.driver.restart(name)
        else:
            module = pluginMgr.plugin(name)
            statuses[name] = module.driver().restart(name)

        return statuses

    # stop all
    def stop(self, command):
        statuses = dict()
        name: str = command.role
        if name == 'all':
            for key, value in pluginMgr.modules().items():
                statuses[key] = value.driver.stop(name)
        else:
            module = pluginMgr.plugin(name)
            statuses[name] = module.driver().stop(name)

        return statuses
