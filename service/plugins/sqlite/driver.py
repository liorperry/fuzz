# File: driver.py
import asyncio
import getopt
import sys

from service.plugins.BaseDriver import baseDriver


class Driver(baseDriver):

	def init(self, args):
		self.output_dir = ''
		self.db = 'dbtest.db'

		try:
			options, remainder = getopt.getopt(args, 'i:o:', ['output=','input=','target-path=','output-dir='])
		except getopt.GetoptError as err:
			print(err)
		for opt, arg in options:
			if opt in ('-o', '--output'):
				self.output_file = arg
			elif opt in ('-i', '--input'):
				self.input_file = arg
			elif opt == '--target-path':
				self.sqlite_path = arg
			elif opt == '--output-dir':
				self.output_dir = arg + '/'

	async def runGenerator(self):
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