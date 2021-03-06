# File: generator.py
import json
import os
import sys

from model.Status import Status
from service.plugins.BaseGenerator import BaseGenerator
from service.plugins.sqlite.randQuery import Randomize


class Generator(BaseGenerator):
	def init_parse(self, args):
		self.randPkg = Randomize()
		self.output_dir = args['output_dir']
		self.template_dir = args['template_dir']
		self.max_file_lines = 50

	def create(self, line):
		tableN = self.randPkg.setNewTable()
		params = self.randPkg.createTableCols(tableN)
		return line.replace('$table_name', tableN).replace('$params', params)

	def alter(self, line):
		oldTable = self.randPkg.getTable()
		newTable = self.randPkg.setNewTable(oldTable)
		return line.replace('$old_table_name', oldTable).replace('$new_table_name', newTable)

	def insert(self, line):
		tableN = self.randPkg.getTable()
		params, numOfCols = self.randPkg.getTableCols('insert',tableN)
		if numOfCols == 0:
			return ''
		vals = self.randPkg.randTableValues(numOfCols)
		return line.replace('$table_name', tableN).replace('$params', params).replace('$values', vals)

	def update(self, line):
		tableN = self.randPkg.getTable()
		setDef, filterDef = self.randPkg.getUpdateSet(tableN)
		if not setDef or not filterDef:
			return ''
		return line.replace('$table_name', tableN).replace('$update_set', setDef).replace('$update_filter', filterDef)

	def select(self, line):
		tableN = self.randPkg.getTable()
		params, numOfCols = self.randPkg.getTableCols('select',tableN)
		matching = self.randPkg.randMatching(tableN)
		return line.replace('$table_name', tableN).replace('$select_params', params).replace('$matching', matching)

	def delete(self, line):
		tableN = self.randPkg.getTable()
		return line.replace('$table_name', tableN)

	def drop(self, line):
		tableN = self.randPkg.dropTable()
		return line.replace('$table_name', tableN)


	def generate(self, runId, command, completeHook):
		currentDir = os.path.dirname(os.path.realpath(__file__))
		with open(os.path.join(currentDir ,"sqlite_template.json"), "r") as read_file:
			json_data = json.load(read_file)

		write_file = ''
		keys = list(json_data.keys())
		rand_num = self.randPkg.getRandNum(1,self.max_file_lines)
		for i in range(rand_num):
			func = self.randPkg.getRandFromList(keys)
			if (func != 'create' and not bool(self.randPkg.map)):
				continue
			data = json_data[func]
			try:
				method = getattr(self, func)
			except AttributeError:
				print('no method: ', func)
				continue
			write_file += method(data) +'\n'

		currentDir = os.path.dirname(os.path.realpath(__file__))
		runDir = os.path.join(currentDir + '/' + self.output_dir + '/' + runId)
		self.metadata.output_dir = os.path.join(runDir, 'sqlite_cmd.sql')
		with open(os.path.join(runDir, 'sqlite_cmd.sql'), 'w') as sql_file:
			sql_file.write(write_file)
		sql_file.close()
		read_file.close()
		# finished callback
		completeHook('sqlite',Status.PASSED)


if __name__== "__main__":
	try:
		gen = Generator(sys.argv[1:])
		gen.generate()
	except Exception as e:
		print('in main: ', e)
