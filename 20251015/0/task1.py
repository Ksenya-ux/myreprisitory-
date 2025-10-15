from  decimal import  Decimal, getcontext

def esum(N, one):
	n = 1
	s = one
	for i in range(1,N+1):
		n *= i
		s += one/n
	print(s)
getcontext().prec=5
esum(30,float(1))
