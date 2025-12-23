class Omnibus:
    _cnt = {}

    def __init__(self):
        object.__setattr__(self, "_has", set())

    def __setattr__(self, name, value):
        if name.startswith("_"): 
            return object.__setattr__(self, name, value)
        if name not in self._has:
            self._has.add(name)
            self._cnt[name] = self._cnt.get(name, 0) + 1

    def __getattr__(self, name):
        if name.startswith("_"): 
            raise AttributeError(name)
        return self._cnt.get(name, 0)

    def __delattr__(self, name):
        if name.startswith("_"):
            try: 
                object.__delattr__(self, name)
            except AttributeError: 
                pass
            return
        if name in self._has:
            self._has.remove(name)
            if name in self._cnt:
                self._cnt[name] -= 1
                if self._cnt[name] <= 0:
                    del self._cnt[name]

import sys
exec(sys.stdin.read())
