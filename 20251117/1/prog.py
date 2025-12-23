def objcount(cls):
    cls.counter = 0

    old_init = getattr(cls, "__init__", None)
    old_del  = getattr(cls, "__del__", None)

    def new_init(self, *args, **kwargs):
        cls.counter += 1
        if old_init:
            old_init(self, *args, **kwargs)

    def new_del(self):
        cls.counter -= 1
        if old_del:
            try:
                old_del(self)
            except:
                pass

    cls.__init__ = new_init
    cls.__del__  = new_del
    return cls

import sys
exec(sys.stdin.read()) 
