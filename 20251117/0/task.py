class Counter:
    def __init__(self):
        self.count = 0
    
    def __get__(self, instance, owner):
        return self.count
    
    def __set__(self, instance, value):
        pass
    
    def __iadd__(self, other):
        self.count += other
        return self
    
    def __isub__(self, other):
        self.count -= other
        return self


class C:
    counter = Counter()
    
    def __init__(self):
        self.counter += 1
    
    def __del__(self):
        self.counter -= 1


c = C()

print(f"c.counter = {c.counter}")

d = C()
print(f"d.counter = {d.counter}")

del c
print(f"d.counter = {d.counter}")
