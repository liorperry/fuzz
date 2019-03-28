# File: driver.py
import asyncio
import sys

from service.plugins.BaseDriver import baseDriver


class Driver(baseDriver):

	def init(self, args):
		self.output_dir = ''
		self.db = 'dbtest.db'
		self.output_file = args['output_file']
		self.input_file = args['input_file']
		self.sqlite_path = args['sqlite_path']
		self.output_dir = args['output_dir']

	async def runFuzzer(self):
		cmd = self.sqlite_path + ' -header -csv '+ self.db +' < '+ self.input_file +' > ' + self.output_file
		proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

		stdout, stderr = await proc.communicate()

		if stdout:
			with open(self.output_dir+'out.txt', 'w') as out:
				out.write(stdout.decode())
		if stderr:
			with open(self.output_dir+'err.txt', 'w') as err:
				err.write(stderr.decode())


def main():
	try:
		_driver = Driver(sys.argv[1:])
		_driver.start()
	except Exception as e:
		print('in main: ', e)

if __name__== "__main__":
	main()

# cmd: py driver.py -i sqlite_cmd.sql -o data.csv --target-path=..\sqlite327\sqlite3.exe