import importlib
import os


# plugins manager for the entire client
class PluginsMgr:
    # scan plugins folder and list plugins
    def __init__(self, workdir='') -> None:
        super().__init__()
        self.currentDir = os.path.dirname(os.path.realpath(__file__))
        self.workdir = workdir
        self.plugins = dict()
        self._modules()

    # get plugins list
    def _plugins(self):
        return next(os.walk(os.path.join(self.currentDir,self.workdir)))[1]

    # instantiate single module
    def _module(self, plugin: str):
        module = importlib.import_module('service.plugins' + '.' + plugin)
        my_class = getattr(module, plugin + 'PluginMetadata')
        return my_class()

    # instantiate modules
    def _modules(self):
        for plug in self._plugins():
            if not plug.startswith('__'):
                module = self._module(plug)
                self.plugins[plug] = module

    # get plugin metadata
    def inspect(self, plugin):
        return self.plugin(plugin).toJson()

    # get modules instances as list
    def modules(self):
        return list(self.plugins.values())

    # get plugins list
    def plugin(self, name):
        return self.plugins[name]
