class Loader:
	def __init__(self, filePath):
		if(os.path.exists(filePath)):
			if(os.path.isdir(filePath)):
				self.dir = filePath
			elif(os.path.isfile(filePath)):
				self.file = filePath

	def load(self):
		f = open(self.file)
		lines = f.readlines()

		for line in lines:
			