a = []
for i in range(4):
	n = 1
	a.append([])
	for j in range(4):
		a[i].append(n)
		n += 1
for i in range(4):
	print()
	for j in range(4):
		print(a[j][i], end=' ')
