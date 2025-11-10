B = type('B', (), {'__v': 0})
A = type('A', (B, ), {'__v': 1})
a = A()
print(a.__v)
