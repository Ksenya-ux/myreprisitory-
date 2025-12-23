class dump(type):
    def __new__(mcls, clsname, bases, dct):
        for name, obj in list(dct.items()):
            if isinstance(obj, type(lambda: 0)):
                def wrapper(*args, __f=obj, __n=name, **kwargs):
                    print(f"{__n}: {args[1:]}, {kwargs}")
                    return __f(*args, **kwargs)
                dct[name] = wrapper
        return type.__new__(mcls, clsname, bases, dct)

import sys
exec(sys.stdin.read())
