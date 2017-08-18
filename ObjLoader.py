import os

class ObjLoader:

	def __init__(self, filePath):
		if os.path.exists(filePath) and os.path.isfile(filePath):
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
		    temp = line.strip('\n')
		    temp = temp.split(' ')
		    if temp:
				if temp[0] == "v":
					vectors.append([temp[2], temp[3], temp[4]])
				elif temp[0] == "f":
					face = [temp[1].split("/"), temp[2].split("/"), temp[3].split("/")]
					faces.append(face)
				elif temp[0] == "vn":
					normal = [temp[1], temp[2], temp[3]]
					normals.append(normal)
				elif temp[0] == "vt":
					uv = [temp[1], temp[2], temp[3]]
					uvs.append(uv)


		return {
			'vectors' : vectors,
			'faces' : faces,
			'normals' : normals,
			'uvs' : uvs
		}

			