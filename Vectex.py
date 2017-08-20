import math

class Vectex:
	
	index = 0

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		self.neighbor = []

	def length:
		return sqrt(self.x * self.x + self.y * self.y + self.z * self.z);
	
	def normalize:
		len = self.length();
		self.x = self.x / len;
		self.y = self.y / len;
		self.z = self.z / len;
	
	def distence(p):
		return math.sqrt((self.x - p.x) * (self.x - p.x) + (self.y - p.y) * (self.y - p.y) + (self.z - p.z) * (self.z - p.z));


	def minus(p):
		newVec = Vectex(self.x - p.x, self.y - p.y, self.z -p.z)
		return newVec

	@staticmethod
	def prod(p1, p2):
		newVec = Vectex(p1.y * p2.z - p2.y * p1.z, p1.z * p2.x - p2.z * p1.x, p1.x * p2.y - p2.x * p1.y);
		return newVec

	@staticmethod
	def dot(p1 ,p2):
		return p1.x * p2.x + p1.y * p2.y + p1.z * p2.z;
