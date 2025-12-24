import sys
import math

def draw_graph(W, H, A, B, formula):
    screen = [[' ' for _ in range(W)] for __ in range(H)]
    
    num_points = W * 4
    xs = [A + (B - A) * i / (num_points - 1) for i in range(num_points)]
    fs = []
    for x in xs:
        try:
            val = eval(formula, {"__builtins__": {}}, {"x": x, "sin": math.sin, "cos": math.cos,
                                                       "tan": math.tan, "exp": math.exp, "log": math.log,
                                                       "sqrt": math.sqrt, "pi": math.pi, "e": math.e})
        except:
            val = float('nan')
        fs.append(val)
    
    valid_fs = [f for f in fs if not math.isnan(f)]
    if not valid_fs:
        print("No valid values")
        return
    min_f = min(valid_fs)
    max_f = max(valid_fs)
    
    if abs(max_f - min_f) < 1e-9:
        max_f = min_f + 1
    
    def to_screen(x, f):
        col = int((x - A) / (B - A) * (W - 1))
        row = int((max_f - f) / (max_f - min_f) * (H - 1))
        col = max(0, min(col, W - 1))
        row = max(0, min(row, H - 1))
        return col, row
    
    for i in range(len(xs) - 1):
        x1, x2 = xs[i], xs[i + 1]
        f1, f2 = fs[i], fs[i + 1]
        if math.isnan(f1) or math.isnan(f2):
            continue
        col1, row1 = to_screen(x1, f1)
        col2, row2 = to_screen(x2, f2)
        steps = max(abs(col2 - col1), abs(row2 - row1)) or 1
        for s in range(steps + 1):
            t = s / steps
            col = int(col1 + (col2 - col1) * t)
            row = int(row1 + (row2 - row1) * t)
            if 0 <= col < W and 0 <= row < H:
                screen[row][col] = '*'
    
    for row in screen:
        print(''.join(row))

if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    if len(data) < 5:
        exec(sys.stdin.read())
    else:
        W, H = int(data[0]), int(data[1])
        A, B = float(data[2]), float(data[3])
        formula = ' '.join(data[4:])
        draw_graph(W, H, A, B, formula)
