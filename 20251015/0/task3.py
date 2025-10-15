from math import*
W, H, A, B = 30, 40, -5, 5
for i in range(H):
	X = A + i * (B - A)/(W-1)
	Y = sin(X)
	w = (1 + Y) * H/2
	print(int(w)*' '+ '*')
