class Triangle:
    def __init__(self, *points):
        self.points = [tuple(p) for p in points]
    
    def __abs__(self):
        if len(self.points) != 3:
            return 0
        
        (x1, y1), (x2, y2), (x3, y3) = self.points
        area = abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2)
        return area
    
    def __bool__(self):
        return abs(self) > 0
    
    def __lt__(self, other):
        return abs(self) < abs(other)
    
    def _contains_point(self, point):
        if not self:
            return False
        
        (x1, y1), (x2, y2), (x3, y3) = self.points
        x, y = point

        def sign(p1, p2, p3):
            return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
        
        d1 = sign((x, y), (x1, y1), (x2, y2))
        d2 = sign((x, y), (x2, y2), (x3, y3))
        d3 = sign((x, y), (x3, y3), (x1, y1))
        
        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
        
        return not (has_neg and has_pos)
    
    def __contains__(self, other):
        if not other:
            return True
        if not self:
            return False

        for point in other.points:
            if not self._contains_point(point):
                return False
        return True
    
    def _segments_intersect(self, p1, p2, q1, q2):
        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0
            return 1 if val > 0 else 2
        
        def on_segment(p, q, r):
            return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
                    min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))
        
        o1 = orientation(p1, p2, q1)
        o2 = orientation(p1, p2, q2)
        o3 = orientation(q1, q2, p1)
        o4 = orientation(q1, q2, p2)
        
        if o1 != o2 and o3 != o4:
            return True

        if o1 == 0 and on_segment(p1, q1, p2):
            return True
        if o2 == 0 and on_segment(p1, q2, p2):
            return True
        if o3 == 0 and on_segment(q1, p1, q2):
            return True
        if o4 == 0 and on_segment(q1, p2, q2):
            return True
        
        return False
    
    def __and__(self, other):
        if not self or not other:
            return False

        for p in self.points:
            if other._contains_point(p):
                return True
        for p in other.points:
            if self._contains_point(p):
                return True

        sides_self = [(self.points[0], self.points[1]),
                      (self.points[1], self.points[2]),
                      (self.points[2], self.points[0])]
        
        sides_other = [(other.points[0], other.points[1]),
                       (other.points[1], other.points[2]),
                       (other.points[2], other.points[0])]
        
        for s1 in sides_self:
            for s2 in sides_other:
                if self._segments_intersect(s1[0], s1[1], s2[0], s2[1]):
                    return True
        
        return False

import sys
exec(sys.stdin.read())

