from math import *

def Calc(s, t, u):
    def func(x):
        t_value = eval(t, globals(), {'x': x})
        s_value = eval(s, globals(), {'x': x})
        result = eval(u, globals(), {'x': s_value, 'y': t_value})
        return result
    return func
    
formul_s, formul_t, formul_u = eval(input())
val = eval(input())
F = Calc(formul_s,formul_t, formul_u)
ans = F(val)
print(ans)
