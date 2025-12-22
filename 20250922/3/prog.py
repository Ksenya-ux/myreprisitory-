def dig_count(x):
    ds = 0
    while x > 0:
        ds += x % 10
        x = x // 10
    return ds

i = 0
while i < 3:
    j = 0
    while j < 3:
        a = n + i
        b = n + j
        pr = a * b
        if dig_count(pr) == 6:
            print(f"{a} * {b} = :)", end="")
        else:
            print(f"{a} * {b} = {pr}", end="")
        if j < 2:
            print(" ", end="")
        j += 1
    print()
    i += 1
