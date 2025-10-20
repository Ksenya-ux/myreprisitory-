x = input().split()
d = {}
d1 = {d.setdefault(i,0) + 1 for i in x}
print(*d.keys())
