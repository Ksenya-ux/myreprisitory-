class Num:
    def __init__(self, start_value=0):
        self._box = {}
        self._default = start_value

    def __get__(self, obj, owner=None):
        if obj is None:
            return self
        return self._box.get(id(obj), self._default)

    def __set__(self, obj, x):
        if hasattr(x, "real"):
            value = x.real
        elif hasattr(x, "__len__"):
            value = len(x)
        else:
            value = x
        self._box[id(obj)] = value

class C:
    num = Num()

import sys
exec(sys.stdin.read())
