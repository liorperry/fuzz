# File: driver.py
import asyncio
import os
import sys

from model.Status import Status
from service.plugins.BaseDriver import baseDriver
from service.utils import TimestampMillisec64


class Driver(baseDriver):

    def init(self, args):
        self.output_dir = ''
        self.db = 'dbtest.db'
        self.output_file = args['output_file']
        self.log_file = args['log_file']
        self.input_file = args['input_file']
        self.sqlite_path = args['sqlite_path']

    async def runFuzzer(self, runId, command, completeHook):
        startTime = TimestampMillisec64()
        currentDir = os.path.dirname(os.path.realpath(__file__))
        # run metadata
        # run params
        self.log_file = os.path.join(self.runDir, 'log_')
        self.db = os.path.join(self.runDir, 'dbtest.db')
        # run batch command
        cmd = currentDir + self.sqlite_path + ' -header -csv ' + self.db + ' < ' + self.metadata.output_dir + ' > ' + self.log_file
        # print('running: ' + cmd)
        proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE,
                                                     stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await proc.communicate()
        num_lines = sum(1 for line in open(self.metadata.output_dir))
        if stdout:
            with open(self.log_file + 'out.txt', 'w') as out:
                out.write(stdout.decode())
                completeHook(self.name(), Status.PASSED, run=runId, command=command, time=startTime, lines=num_lines)
        if stderr:
            with open(self.log_file + 'err.txt', 'w') as err:
                err.write(stderr.decode())
                completeHook(self.name(), Status.ERROR, run=runId, command=command, time=startTime, lines=num_lines)

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
