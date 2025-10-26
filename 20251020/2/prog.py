import sys
from math import *

cnt = 0
f_dict = {}

def quit_func(fmt):
    return fmt.format(len(f_dict), cnt)

f_dict['quit'] = (quit_func, 1)

while True:
    s = sys.stdin.readline().strip()
    if not s:
        continue
    cnt += 1

    if s[0] == ':':
        parts = s.split()
        name = parts[0][1:]
        vars = parts[1:-1]
        ex = parts[-1]
        
        def make_f(vars, ex):
            def f(*args):
                loc = {}
                for i in range(len(vars)):
                    try:
                        loc[vars[i]] = eval(args[i])
                    except:
                        loc[vars[i]] = args[i]
                return eval(ex, globals(), loc)
            return f
        
        f_dict[name] = (make_f(vars, ex), len(vars))
    else:
        parts = s.split()
        name = parts[0]
        
        if name not in f_dict:
            continue
            
        func, n_vars = f_dict[name]
        
        if n_vars == 0:
            print(func())
        elif n_vars == 1:
            arg_s = s[len(name):].strip()
            if arg_s.startswith('"') and arg_s.endswith('"'):
                arg_s = arg_s[1:-1]
            print(func(arg_s))
        else:
            args = parts[1:]
            print(func(*args))
            
    if s.startswith('quit'):
        break
