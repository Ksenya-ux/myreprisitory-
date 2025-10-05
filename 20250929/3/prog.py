s = input()
m = []
ans = []
while s != '':
    s = s.split(',')
    s = [int(i) for i in s]
    m.append(s)
    s = input()
n = len(m) // 2
m1 = m[:n]
m2 = m[n:]
ans = []
for i in range(n):
    temp = []
    for j in range(n):
        st = 0
        for k in range(n):
            st += m1[i][k] * m2[k][j]
        temp.append(st)
    ans.append(temp)
for i in ans:
    print(*i)
