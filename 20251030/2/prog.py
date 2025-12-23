class Triangle:
    def __init__(self, a,b,c):
        self.a, self.b, self.c = tuple(a), tuple(b), tuple(c)

    def _area2(self):
        ax,ay = self.a; bx,by = self.b; cx,cy = self.c
        return abs((bx-ax)*(cy-ay) - (by-ay)*(cx-ax))

    def __abs__(self):   return self._area2() / 2.0
    def __bool__(self):  return self._area2() != 0
    def __lt__(self, o): return abs(self) < abs(o)

    def __contains__(self, o):
        if not o: return True
        if not self: return False
        A,B,C = self.a,self.b,self.c
        def a2(p,q,r):
            return abs((q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0]))
        def inside(p):
            S  = a2(A,B,C)
            return a2(p,B,C)+a2(A,p,C)+a2(A,B,p) == S
        return inside(o.a) and inside(o.b) and inside(o.c)

    def __and__(self, o):
        if (not self) or (not o): return False
        A,B,C = self.a,self.b,self.c
        D,E,F = o.a,o.b,o.c

        def ori(p,q,r):
            s = (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])
            return 0 if s==0 else (1 if s>0 else -1)
        def on_seg(p,q,r):
            if ori(p,q,r)!=0: return False
            return min(p[0],q[0])<=r[0]<=max(p[0],q[0]) and min(p[1],q[1])<=r[1]<=max(p[1],q[1])
        def seg_int(p1,q1,p2,q2):
            o1,o2 = ori(p1,q1,p2), ori(p1,q1,q2)
            o3,o4 = ori(p2,q2,p1), ori(p2,q2,q1)
            if o1==0 and on_seg(p1,q1,p2): return True
            if o2==0 and on_seg(p1,q1,q2): return True
            if o3==0 and on_seg(p2,q2,p1): return True
            if o4==0 and on_seg(p2,q2,q1): return True
            return (o1*o2<0) and (o3*o4<0)

        E1=[(A,B),(B,C),(C,A)]; E2=[(D,E),(E,F),(F,D)]
        for (p1,q1) in E1:
            for (p2,q2) in E2:
                if seg_int(p1,q1,p2,q2): return True
        return (o in self) or (self in o)

import sys
exec(sys.stdin.read())
