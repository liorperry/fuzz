from service import pluginMgr
from service.LifeCycleApi import LifeCycleApi


class ExternalApiService(LifeCycleApi):

    def __init__(self):
        super().__init__()

    def run(self, command):
        statuses = dict()
        name: str = command.getRole()
        if name == 'all':
            for key, value in pluginMgr.modules().items():
                statuses[key] = value.driver.run(command)
        else:
            module = pluginMgr.plugin(name)
            statuses[name] = module.driver().run(command)

        return statuses

    # pause all
    def pause(self, command):
        statuses = dict()
        name: str = command.getRole()
        if name == 'all':
            for key, value in pluginMgr.modules().items():
                statuses[key] = value.driver.pause(command)
        else:
            module = pluginMgr.plugin(name)
            statuses[name] = module.driver().pause(command)

        return statuses

    # restart all
    def restart(self, command):
        statuses = dict()
        name: str = command.getRole()
        if name == 'all':
            for key, value in pluginMgr.modules().items():
                statuses[key] = value.driver.restart(command)
        else:
            module = pluginMgr.plugin(name)
            statuses[name] = module.driver().restart(command)

        return statuses

    # stop all
    def stop(self, command):
        statuses = dict()
        name: str = command.getRole()
        if name == 'all':
            for key, value in pluginMgr.modules().items():
                statuses[key] = value.driver.stop(command)
        else:
            module = pluginMgr.plugin(name)
            statuses[name] = module.driver().stop(command)

        return statuses
