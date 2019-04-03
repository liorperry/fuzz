from model.ManagerStatus import MyManagerStatus
from model.ProgUnderTestStatus import ProgUnderTestStatus

from service.plugins import PLUGINS
from service.plugins.PluginsManager import PluginsMgr

statusMgr = MyManagerStatus()
pluginMgr = PluginsMgr()

from service.ApiService import ExternalApiService
apiService = ExternalApiService()


def init():
    for module in pluginMgr.modules():
        statusMgr.add(ProgUnderTestStatus(vars(module)))
