from fractions import Fraction

def eval_func(coeffs, x):
    res = Fraction(0)
    for cur in coeffs:
        res = res * x + cur
    return res

def reorg(data) -> bool:
    
    s = data[0]
    w = data[1]
    d_a = int(data[2])
    k_a = data[3:3+d_a+1]
    d_b = int(data[3+d_a+1])
    k_b = data[3+d_a+2:3+d_a+2+d_b+1]
    
    k_a1 = [Fraction(k.strip()) for k in k_a]
    k_b1 = [Fraction(k.strip()) for k in k_b]
    
    a_val = eval_func(k_a1, Fraction(s.strip()))
    b_val = eval_func(k_b1, Fraction(s.strip()))
    
    if b_val == 0:
        return False
    return a_val / b_val == Fraction(w.strip())

inp = [i.strip() for i in input().split(",")]
print(reorg(inp))
