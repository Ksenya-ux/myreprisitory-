n1,n2 = int(input()), int(input())
print([i for i in range(n1, n2) if (i % 2 and '3' in str(i)) ])
