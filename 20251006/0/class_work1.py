def rec(x):
	if x == 1:
		return 'ok'
	print(x)
	return rec(x-1)
print(rec(10))
