import sys
from math import *

def Calc(s, t, u):
    def func(x):
        t_value = eval(t, globals(), {'x': x})
        s_value = eval(s, globals(), {'x': x})
        result = eval(u, globals(), {'x': s_value, 'y': t_value})
        return result
    return func

data = sys.stdin.read().strip()

if not data:
    print("Ошибка: ввод пуст")
    sys.exit(1)


lines = data.split('\n')

try:

    formul_s, formul_t, formul_u = eval(lines[0])
    

    val = eval(lines[1])
    
    F = Calc(formul_s, formul_t, formul_u)
    ans = F(val)
    print(ans)
    
except IndexError:
    print("Ошибка:")
except (SyntaxError, ValueError) as e:
    print(f"Ошибка в формате ввода: {e}")
except Exception as e:
    print(f"Ошибка вычисления: {e}")
