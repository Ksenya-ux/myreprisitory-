from math import*
W, H, A, B = 60, 20, -10, 10
def scale(a,b,A,B,x):
	X = (B - A) * (x-a) / (b-a) + A
	return X
scr = [['.']* W for i in range(H)]
for i in range(W):
	X = scale(0,W
	-1,A,B,i)
	Y = sin(X)
	w = int(scale(-1,1,H-1,0,Y))
	scr[w][i] = '*'
print('\n'.join([''.join(line) for line in scr]))
