def summ():
	i = 1
	n = 0
	while True:
		n += 1/(i**2)
		yield n
		i += 1

a = next(summ)
