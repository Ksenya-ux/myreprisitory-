def Pareto(pairs):
    pareto_front = []
    for i, (x, y) in enumerate(pairs):
        d = False
        for j, (a, b) in enumerate(pairs):
            if a >= x and b >= y and (a > x or b > y):
                d = True
                break  
        if not d:
            pareto_front.append((x, y))
    
    return tuple(pareto_front)
inp = eval(input())
print(Pareto(inp))
