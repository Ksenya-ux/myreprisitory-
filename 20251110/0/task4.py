class A:
	def __init__(self,a):
		print('A:')
		return a
class B(A):
	def __init__(self,b):
		print('B:')
		return super().__init__(b)
class C(B):
	def __init__(self,c):
		print('C:')
		return super.__init(c)
