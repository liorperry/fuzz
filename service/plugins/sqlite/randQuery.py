# File: randQuery.py
import random
import string

# TODO: 
# sqlite FTS expressions should be extended with count(*), 'order by', 'group by' etc.

class Randomize:
	def __init__(self):
		self.map = {}
	
	def getRandNum(self, minRange, maxRange):
		return random.randint(minRange, maxRange)

	def getRandString(self):
		strlen = self.getRandNum(1,10)
		# phase 1: just letters & digits, without 'string.punctuation'
		# table name & columns' name cannot start with numeric char 
		return random.choice(string.ascii_letters) + ''.join(random.choices(string.ascii_letters + string.digits, k=strlen-1))

	def getRandFromList(self, list, itemsNum=1):
		if (itemsNum ==1):
			return random.choice(list)
		else:
			return random.sample(list, itemsNum)

	def setNewTable(self, oldTable = None):
		tableName = self.getRandString()
		if oldTable is not None:
			self.map[tableName] = self.map.pop(oldTable)
		else:
			self.map[tableName] = []
		return tableName

	def getTable(self):
		tableName = None if not bool(self.map) else self.getRandFromList(list(self.map.keys()))
		return tableName

	def dropTable(self, tableName = None):
		if not tableName:
			tableName = self.getTable()
		del self.map[tableName]
		return tableName

	def createTableCols(self, tableName):
		numOfCols = self.getRandNum(0,5)
		cols = []
		for i in range(numOfCols):
			cols.append(self.getRandString())
		self.map[tableName] = cols
		return ', '.join(cols)

	def getTableCols(self, funcName, tableName):
		maxCols = len(self.map[tableName])
		if maxCols == 0:
			return '*', 0
		numOfCols = self.getRandNum(1,maxCols)
		if numOfCols == maxCols and funcName == 'select':
			return '*', maxCols
		cols = self.getRandFromList(self.map[tableName], numOfCols)
		if numOfCols == 1:
			return cols, numOfCols
		return ', '.join(cols) , numOfCols

	def randTableValues(self, numOfCols):
		numOfRows = self.getRandNum(1,10)
		valsForInsert = []
		for r in range(numOfRows):
			rowVals = []
			for c in range(numOfCols):
				rowVals.append(self.getRandString())
			valsForInsert.append("('"+"', '".join(rowVals)+"')")
		return ', '.join(valsForInsert)

	# TODO: the values of MATCH should be extended
	def randMatching(self, tableName):
		randDecision = self.getRandNum(0,2)
		tableCols = self.map[tableName]
		if randDecision == 0 or not tableCols :
			return ''
		val = self.getRandString()
		if randDecision == 1:
			return "WHERE " + tableName + " MATCH '" + val + "'"
		columnName = self.getRandFromList(tableCols)
		if randDecision == 2:
			return "WHERE " + columnName + " MATCH '" + val + "'"

	def getUpdateSet(self, tableName):
		colsList = self.map[tableName]
		if not colsList:
			return None , None
		colsList = random.choices(colsList, k=2)
		setDef = colsList[0] + " = '" + self.getRandString() + "'"
		filterDef = colsList[1] + " = '" + self.getRandString() + "'"
		return setDef, filterDef


# if __name__== "__main__":
	# r = Randomize()
