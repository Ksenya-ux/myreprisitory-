x = int(input())

for i in range(3):
    for j in range(3):
        p = x + i
        q = x + j
        r = p * q
        
        t = r
        v = 0
        while t > 0:
            v += t % 10
            t //= 10
        
        if v == 6:
            print(f"{p} * {q} = :=)", end="")
        else:
            print(f"{p} * {q} = {r}", end="")
        
        if j < 2:
            print(" ", end="")
    
    print()
