class A: pass
class B: pass
class C(A, B): pass
class D(B, A): pass
c = 6
for i in [A, B, D]:
	try:
		class E(C,i): pass
	except:
		c -= 1
for i in [A, B, D]:
	try:
		class E(i,C): pass
	except:
		c -= 1
print(c)
