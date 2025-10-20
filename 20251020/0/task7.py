a, b = int(input()), int(input())
s = input()
print(eval(s,  globals(), {'x' : a, 'y' : b}))
