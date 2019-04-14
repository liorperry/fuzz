# File: generator.py

from model.Status import Status
from service.plugins.BaseGenerator import BaseGenerator


class Generator(BaseGenerator):

    def init_parse(self, args):
        self.output_dir = args['output_dir']
        self.template_dir = args['template_dir']

    def generate(self, runId, command, completeHook):
        # finished callback
        completeHook('sqlite', Status.PASSED)
