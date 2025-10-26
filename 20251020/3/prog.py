num = int(input())
s = input().lower()
data = ''
ans = {}
while s:
    for i in s:
        if i.isalpha() == False:
            s = s.replace(i,' ')
    data += s
    s = input().lower()
data = data.split()
for i in data:
    if len(i) == num and i not in ans.keys():
        ans[i] = 1
    elif len(i) == num:
        ans[i] += 1
res = []
m = 0
for i in ans.keys():
    if ans.get(i) > m:
        m = ans.get(i)
        res = []
        res.append(i)
    elif ans.get(i) == m:
        res.append(i)
    
print(*sorted(res))
