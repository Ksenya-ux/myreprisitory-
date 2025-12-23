class Maze:
    def __init__(self, n):
        self.n = n
        self.h = [[False]*(n-1) for _ in range(n)]
        self.v = [[False]*n       for _ in range(n-1)]

    def _unpack(self, key):
        if isinstance(key, slice):
            (x0,y0), (x1,y1) = key.start, key.stop
            return (x0,y0), (x1,y1)
        if isinstance(key, tuple) and len(key)==3 and isinstance(key[1], slice):
            x0 = key[0]; y0 = key[1].start; x1 = key[1].stop; y1 = key[2]
            return (x0,y0), (x1,y1)
        raise TypeError("bad index")

    def _open_close_line(self, a,b, ch):
        (x0,y0),(x1,y1) = a,b
        if x0==x1:
            if y0>y1: y0,y1 = y1,y0
            for y in range(y0, y1):
                self.v[y][x0] = (ch=='·')
        elif y0==y1:
            if x0>x1: x0,x1 = x1,x0
            for x in range(x0, x1):
                self.h[y0][x] = (ch=='·')
        else:
            return

    def __setitem__(self, key, val):
        a,b = self._unpack(key)
        self._open_close_line(a,b, val)

    def __getitem__(self, key):
        (x0,y0), (x1,y1) = self._unpack(key)
        n = self.n
        seen=set(); st=[(x0,y0)]
        while st:
            x,y = st.pop()
            if (x,y) in seen: continue
            seen.add((x,y))
            if (x,y)==(x1,y1): return True
            if x>0   and self.h[y][x-1]: st.append((x-1,y))
            if x<n-1 and self.h[y][x]  : st.append((x+1,y))
            if y>0   and self.v[y-1][x]: st.append((x,y-1))
            if y<n-1 and self.v[y][x]  : st.append((x,y+1))
        return False

    def __str__(self):
        n = self.n
        H,W = 2*n+1, 2*n+1
        g = [['█']*W for _ in range(H)]
        for y in range(n):
            for x in range(n):
                g[2*y+1][2*x+1] = '·'
        for y in range(n):
            for x in range(n-1):
                if self.h[y][x]: g[2*y+1][2*x+2] = '·'
        for y in range(n-1):
            for x in range(n):
                if self.v[y][x]: g[2*y+2][2*x+1] = '·'
        return '\n'.join(''.join(r) for r in g)

import sys
exec(sys.stdin.read())
