sum = 0
n = int(input())
while n > 0:
	sum += n
	if sum > 21:
		print(sum)
		break
	n = int(input())
else:
	print(n)
