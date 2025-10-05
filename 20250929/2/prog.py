a = input().split(',')
x = [int(i) for i in a]
for i in range(len(x)):
    for j in range(0, len(x) - i - 1):
        if ((x[j]**2) % 100) > ((x[j+1]**2) % 100):
            x[j], x[j+1] = x[j+1], x[j]
print(x)
