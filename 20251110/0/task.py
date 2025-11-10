class A:
	def __init__(self,val):
		self.val = val
	def __add__(self,other):
		returm self.__class__(self.val+other.val)
class B(A):
	pass
