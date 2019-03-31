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

    # get plugins list
    def plugin(self, name):
        list = next(os.walk(self.workdir))[1]
        return self.module(list[list.index(name)])

    # get plugin metadata
    def inspect(self, plugin):
        return self.module(plugin).toJson()

    def module(self, plugin : str):
        if not plugin.startswith('__'):
           module = importlib.import_module('service.plugins' +'.' + plugin)
           my_class = getattr(module, plugin +'PluginMetadata')
           return my_class()


    def modules(self):
        return list(map(lambda p: self.module(p), self.plugins()))


