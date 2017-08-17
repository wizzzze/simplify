import os

class Loader:
	
	files = [];

	def load(self, path):
		if os.path.isdir(path):
			pathDir =  os.listdir(path)
    		for childPath in pathDir:
        		child = os.path.join('%s%s' % (path, childPath))
        		if os.path.isdir(child):
        			childrenFiles = self.loader(child)
        		elif os.path.isfile(child):
        			self.files.append(child) 
        		else :
        			continue

		else :
			self.files.append(path)
		
		return self.files


		