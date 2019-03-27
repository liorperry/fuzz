import importlib
import os


class PluginsMgr:
    # todo scan plugins folder and list plugins
    def __init__(self, workdir='.') -> None:
        super().__init__()
        self.workdir = workdir

    # get plugins list
    def plugins(self):
        return next(os.walk(self.workdir))[1]

    # get plugin metadata
    def inspect(self, plugin):
        module = importlib.import_module('service.plugins' +'.' + plugin)
        my_class = getattr(module, plugin +'PluginMetadata')
        return my_class().toJson()

