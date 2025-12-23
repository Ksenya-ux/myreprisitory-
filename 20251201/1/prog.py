class dump(type):
    def __new__(mcs, name, bases, ns):
        for attr_name, attr_value in ns.items():
            if callable(attr_value):
                def make_wrapper(method):
                    def wrapper(self, *args, **kwargs):
                        filtered_args = tuple(arg for arg in args 
                                           if isinstance(arg, (str, int, float, bool)))
                        filtered_kwargs = {k: v for k, v in kwargs.items() 
                                         if isinstance(v, (str, int, float, bool))}
                        print(f"{method.__name__}: {filtered_args}, {filtered_kwargs}")
                        return method(self, *args, **kwargs)
                    wrapper.__name__ = method.__name__
                    return wrapper
                
                ns[attr_name] = make_wrapper(attr_value)
        
        return super().__new__(mcs, name, bases, ns)


import sys
exec(sys.stdin.read())
