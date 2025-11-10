A = type('A', (str, ), {'__init__' : lambda self, x: setattr(self,'a',x), '__str__' :  lambda self: str(self.a)})
c =  A(4)
print(c)
