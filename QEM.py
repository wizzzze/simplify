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
		Point norm = prod(self.vecteies[tri.poin[1]] - self.vecteies[tri.point[0]], self.vecteies[tri.point[2]] - self.vecteies[tri.point[0]]);
		norm.normalize();
		double p[4] = {norm.x, norm.y, norm.z, dot(norm, *(tri->p[0])) * (-1)};
		for(int i = 0; i < 4; i++for(int j = 0; j < 4; j++) { 
			a[i][j] = p[i] * p[j];
		}




