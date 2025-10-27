from itertools import islice, dropwhile
def summ():
	i = 1
	n = 0
	while True:
		n += 1/(i**2)
		yield n
		i += 1

print(*islice(dropwhile(lambda x: x < 1.6, summ()),10))
