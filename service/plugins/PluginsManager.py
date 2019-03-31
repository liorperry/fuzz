import importlib
import os

from service.plugins.BasePluginMetadata import BasePluginMetadata


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
       module = importlib.import_module('service.plugins' +'.' + plugin)
       my_class = getattr(module, plugin +'PluginMetadata')
       return my_class()


    def modules(self):
        li = []
        for plug in self.plugins():
            if not plug.startswith('__'):
                    li.append(self.module(plug))
        return li

