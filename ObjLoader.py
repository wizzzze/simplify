import os
import re

class ObjLoader:

	def __init__(self, filePath):
		if os.path.exists(filePath) and os.path.isfile(filePath):
			self.file = filePath

	def load(self):
		f = open(self.file)
		lines = f.readlines()
		f.close();
		vecteies = []
		faces = []
		normals = []
		uvs = []

		for line in lines:
		    temp = line.strip('\n')
		    temp = temp.split(' ')
		    if temp:
				if temp[0] == "v":
					vectex = Vectex(temp[2], temp[3], temp[4])
					vecteies.append(vectex)
					vectex.index = len(vecteies)
				elif temp[0] == "f":
					p0 = temp[1].split("/")
					p1 = temp[2].split("/")
					p2 = temp[3].split("/")

					tri = Tri(p0, p1, p2, vecteies[p0-1] ,vecteies[p1-1], vecteies[p2-1])
					for point in tri.points:
						if not point.belongToTri:
							point.belongToTri = []
						else:
							point.belongToTri.appen(tri)

					tri.index = len(faces)

					faces.append(tri)
				elif temp[0] == "vn":
					normal = [temp[1], temp[2], temp[3]]
					normals.append(normal)
				elif temp[0] == "vt":
					uv = [temp[1], temp[2], temp[3]]
					uvs.append(uv)
				else
					continue


		return {
			'vecteies' : vecteies,
			'faces' : faces,
			'normals' : normals,
			'uvs' : uvs
		}

			