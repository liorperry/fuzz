from model.ManagerStatus import MyManagerStatus
from model.ProgUnderTestStatus import ProgUnderTestStatus

from service.plugins import PLUGINS
from service.plugins.PluginsManager import PluginsMgr

manager = MyManagerStatus()
modules = dict()

from service.ApiService import ExternalApiService
apiService = ExternalApiService()


def init():
    for module in PluginsMgr(PLUGINS).modules():
        modules[module.name] = module
        manager.add(ProgUnderTestStatus(vars(module)))
