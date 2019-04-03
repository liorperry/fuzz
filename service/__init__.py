from model.ManagerStatus import MyManagerStatus
from service.RepeatedTimer import RepeatedTimer
from service.plugins import PLUGINS
from service.plugins.PluginsManager import PluginsMgr

statusMgr = MyManagerStatus()
pluginMgr = PluginsMgr(statusMgr)

from service.ApiService import ExternalApiService
apiService = ExternalApiService()


def init():
    # start status updated
    rt = RepeatedTimer(5, statusMgr.updateStatus)  # it auto-starts, no need of rt.start()
    rt.start()
