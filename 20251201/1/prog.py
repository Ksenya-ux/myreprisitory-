import sys

class dump(type):
    def __new__(mcs, name, bases, namespace):
        for attr_name, attr_value in namespace.items():
            if callable(attr_value) and not attr_name.startswith('_'):
                namespace[attr_name] = mcs.wrapper(attr_value, attr_name)
        return super().__new__(mcs, name, bases, namespace)
    
    @staticmethod
    def wrapper(method, name):
        def wrapped(*args, **kwargs):
            print(f"{name}: {args[1:]}, {kwargs}")
            return method(*args, **kwargs)
        return wrapped

exec(sys.stdin.read())
