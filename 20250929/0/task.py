a = []
for i in range(4):
	n = 1
	a.append([])
	for j in range(4):
		n += 1
		a[i].append(n)

for i in range(4):
	for j in range(4):
		a[i][j] = a[j][i]
