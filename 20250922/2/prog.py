sum = 0
while n > 0:
	sum += n
	if sum > 21:
		print(sum)
		break
	n = int(input())
else:
	print(n)
