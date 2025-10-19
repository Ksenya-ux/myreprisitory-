from math import *
inp  = [i.strip() for i in input().split()]
W, H, A, B, f = int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3]), inp[4]
A, B = int(A), int(B)
def scale(a,b,A,B,x):
    X = (B - A) * (x-a) / (b-a) + A
    return X
scr = [[' ']* W for i in range(H)]
for i in range(W):
    X = scale(0,W-1,A,B,i)
    Y = eval(f, {'x': X, **globals()})
    w = int(scale(-1,1,H-1,0,Y))
    scr[w][i] = '*'
print('\n'.join([''.join(line) for line in scr]))
