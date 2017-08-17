import os

class Loader:
	
	files = [];

	def __init__(self, filePath):
		if(os.path.exists(filePath)):
			if(os.path.isdir(filePath)):
				self.dir = filePath
			elif(os.path.isfile(filePath)):
				self.file = filePath

	def loader(self, path):
		if(os.path.isdir(path)):
			pathDir =  os.listdir(path)
    		for path in pathDir:
        		child = os.path.join('%s%s' % (filepath, path))
        		if(os.path.isdir(child)):
        			childrenFiles = self.loader(path)
        		elif(os.path.isfile(child)):
        			self.files.append(child);		

        	return self.files
		elif(os.path.isfile(path)):


	def loadFilePath(self):
		