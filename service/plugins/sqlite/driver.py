# File: driver.py
import asyncio
import os
import sys

from model.Status import Status
from service.plugins.BaseDriver import baseDriver


class Driver(baseDriver):

    def init(self, args):
        self.output_dir = ''
        self.db = 'dbtest.db'
        self.output_file = args['output_file']
        self.log_file = args['log_file']
        self.input_file = args['input_file']
        self.sqlite_path = args['sqlite_path']

    async def runFuzzer(self, runId, command, completeHook):
        currentDir = os.path.dirname(os.path.realpath(__file__))
        self.log_file = os.path.join(self.runDir, 'log_')
        self.db = os.path.join(self.runDir, self.db)

        cmd = currentDir + self.sqlite_path + ' -header -csv ' + self.db + ' < ' + self.metadata.output_dir + ' > ' + self.log_file
        proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await proc.communicate()

        if stdout:
            with open(self.log_file + 'out.txt', 'w') as out:
                out.write(stdout.decode())
                completeHook(self.name(),Status.PASSED)
        if stderr:
            with open(self.log_file + 'err.txt', 'w') as err:
                err.write(stderr.decode())
                completeHook(self.name(),Status.ERROR)

    def name(self):
        return 'sqlite'


def main():
    try:
        _driver = Driver(sys.argv[1:])
        _driver.start()
    except Exception as e:
        print('in main: ', e)


if __name__ == "__main__":
    main()

# cmd: py driver.py -i sqlite_cmd.sql -o data.csv --target-path=..\sqlite327\sqlite3.exe
