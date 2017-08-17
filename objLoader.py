class ObjLoader:

	def __init__(self, filePath):
		if os.path.exists(filePath) and os.path.isfile(filePath):
			self.file = filePath

	def load(self):
		f = open(self.file)
		lines = f.readlines()
		f.close();
		vectors = []
		face = []
		normals = []
		uv = []

		for line in lines:
		    temp = line.split(" ")
		    if temp:
				if temp[0] == "v":
					vectors.append(temp[2])
					vectors.append(temp[3])
					vectors.append(temp[4])
				elif temp[0] == "f":
					face.append(temp[2].split("/"))
					face.append(temp[3].split("/"))
					face.append(temp[4].split("/"))
				elif temp[0] == "vn":
					normals.append(temp[2])
					normals.append(temp[3])
					normals.append(temp[4])
				elif temp[0] == "vt":
					uv.append(temp[2])
					uv.append(temp[3])
					uv.append(temp[4])

			