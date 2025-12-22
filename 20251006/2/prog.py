import sys

def sub(x, y):
    if type(x) != type(y):
        raise TypeError('у объектов разный тип данных!')
    if isinstance(x, list):
        ans = []
        for i in x:
            if i not in y:
                ans.append(i)
    elif isinstance(x, tuple):
        ans = []
        for i in x:
            if i not in y:
                ans.append(i)
        ans = tuple(ans)
    elif isinstance(x, (float, int, complex)):
        ans = x - y
    else:
        raise TypeError('неподдерживаемый тип данных')
    return ans


data = sys.stdin.read().strip()

try:
    inp1, inp2 = eval(data) if data else (None, None)
    result = sub(inp1, inp2)
    print(result)
except ValueError:
    print("Ошибка: требуется два значения через запятую")
except TypeError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")
