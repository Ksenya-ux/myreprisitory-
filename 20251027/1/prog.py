def fib(m,n):
    a = [1,1]
    for i in range(2, m + n ):
        if i >= m:
            yield a[i-1]+a[i-2]
        a.append(a[i-2]+a[i-1])
     
