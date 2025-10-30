class rectangle():
	rectnt = 0
	def __init__(self, x1,x2,y1,y2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		rectangle.rectnt += 1
		self.__dict__['rect_k'] = 1
	def __str__(self):
		return f"{self.x1,self.y1} and {self.x2,self.y2}; {self.rectnt}"
	def __abs__(self):
		s1 = self.x2- self.x1
		s2 = self.y2 - self.y1
		s = s1 * s2
		return s
	def __lt__(self,other):
		return abs(self) < abs(other)
	def __eq__(self,other):
		return abs(self) == abs(other)
	def __mul__(self, other):
		return rectangle(self.x1*other.x1, self.x2*other.x2, self.y1*other.y1, self.y2*other.y2)
	__rmul__ = __mul__
	def __getitem__(self, idx):
		spisok = [(self.x1,self.y1), (self.x1,self.y2), (self.x2, self.y1), (self.x2,self.y2)]
		return spisok[idx]
	def __bool__(self):
		if abs(self) == 0:
			return False
		else:
			return True
	def __del__(self):
		return rectangle.rectnt - 1
r1, r2 = rectangle(1,2,3,4), rectangle(2,3,4,5)	
print(r1 * r2)
print(r1[2])
print(bool(r1))
print(del(r1))
