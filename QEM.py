class QEM:

	wightOrder = []
	def toLowPloy(self, data):

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

		
		
		for vi in reverseIndex:
			faces = reverseIndex[vi]
			





