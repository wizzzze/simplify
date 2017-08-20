from numpy import *

class QEM:

	vecteies

	def toLowPloy(self, data):

		vCount = len(data['vecteies'])
		self.vecteies = data['vecteies']
		lowCount = vCount/10

		flength = len(data['faces'])
		fi = 0;
		reverseIndex = {}
		while fi < flength:
			face = data['faces'][fi];
			print face
			for vec in face:
				vindex = int(vec[0])
				if vindex in reverseIndex:
					reverseIndex[vindex].append(fi)
				else:
					reverseIndex[vindex] = [fi]
			fi += 1

		
		
		for face in data['faces']:
			n,m = 0
			ppT = [
				[0,0,0,0],
				[0,0,0,0],
				[0,0,0,0],
				[0,0,0,0]
			]
		
			ppT = self.computerPPT(face, ppT);


		
	


	def computerPPT(tri , ppT) :
		norm = Vectex.prod(self.vecteies[tri.poin[1]].minus(self.vecteies[tri.point[0]]), self.vecteies[tri.point[2]].minus(self.vecteies[tri.point[0]]));
		norm.normalize();
		p = [norm.x, norm.y, norm.z, Vectex.dot(norm, *(tri.point[0])) * (-1)];
		for i in p:
			for j in p 
				ppT[i][j] = p[i] * p[j];
		




