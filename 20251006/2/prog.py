def sub(x,y):
    if type(x) != type(y):
        raise TypeError('у объектов разный тип данных!')
    if isinstance(x, list):
        ans = list()
        for i in x:
            if i not in y:
                ans.append(i)
    if isinstance(x, tuple):
        ans = list()
        for i in x:
            if i not in y:
                ans.append(i)
        ans = tuple(ans)
    if isinstance(x, (float,int, complex)):
        ans = x - y
    return ans
inp1,inp2 = eval(input())
res  = sub(inp1, inp2)
print(res)
