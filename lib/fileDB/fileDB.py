import json
from bson import json_util
class FileDB():
	def __init__(self, filenameList):
		self.fileList=list()
		self.fileIndex=0
		for filename in filenameList:
			self.fileList.append(open(filename, "r"))
	def parseLine(self, line):
		line=line.replace("\n", "")
		session=json.loads(line, object_hook=json_util.object_hook)
		x=session["x"]
		y=session["y"]
		currentTime=session["currentTime"]
		return x, y, currentTime.replace(tzinfo=None)
	def next(self):
		line=self.fileList[self.fileIndex].readline()
		if line=='':
			self.fileIndex+=1
			if not self.fileIndex<len(self.fileList):
				raise StopIteration
			else:
				return self.next()
		else:
			return self.parseLine(line)
	def close(self):
		for file in self.fileList:
			file.close()
