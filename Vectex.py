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
		x = self.x / len;
		y = self.y / len;
		z = self.z / len;
	
	def distence(p):
		return math.sqrt((self.x - p.x) * (self.x - p.x) + (self.y - p.y) * (self.y - p.y) + (self.z - p.z) * (self.z - p.z));