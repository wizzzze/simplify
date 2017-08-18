import os

class ObjLoader:

	def __init__(self, filePath):
		# if os.path.exists(filePath) and os.path.isfile(filePath):
			self.file = filePath

	def load(self):
		f = open(self.file)
		lines = f.readlines()
		f.close();
		vectors = []
		faces = []
		normals = []
		uvs = []

		for line in lines:
		    temp = line.split(" ")
		    if temp:
				if temp[0] == "v":
					vectors.append(temp[2])
					vectors.append(temp[3])
					vectors.append(temp[4])
				elif temp[0] == "f":
					faces.append(temp[2].split("/"))
					faces.append(temp[3].split("/"))
					faces.append(temp[4].split("/"))
				elif temp[0] == "vn":
					normals.append(temp[2])
					normals.append(temp[3])
					normals.append(temp[4])
				elif temp[0] == "vt":
					uvs.append(temp[2])
					uvs.append(temp[3])
					uvs.append(temp[4])


		return {
			'vectors' : vectors,
			'faces' : faces,
			'normals' : normals,
			'uvs' : uvs
		}

			