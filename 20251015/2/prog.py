import math

W, H, a, b, formula = map(str.strip, input().split())
W, H = int(W), int(H)
a, b = float(a), float(b)

def f(x):
    return eval(formula, {"x": x, "math": math, "builtins": {}})

y_vals = []
x_vals = []
for i in range(W):
    x_val = a + (b - a) * i / (W - 1)
    try:
        y = f(x_val)
        if not (math.isnan(y) or math.isinf(y)):
            y_vals.append(y)
            x_vals.append(x_val)
    except:
        pass

if not y_vals:
    y_min, y_max = 0, 1
else:
    y_min, y_max = min(y_vals), max(y_vals)
    if y_min == y_max:
        y_min -= 1
        y_max += 1

grid = [[' ' for _ in range(W)] for _ in range(H)]

points = []
for i in range(W):
    x_val = a + (b - a) * i / (W - 1)
    try:
        y = f(x_val)
        if math.isnan(y) or math.isinf(y):
            points.append(None)
            continue
        row_idx = int((y - y_min) / (y_max - y_min) * (H - 1))
        row_idx = max(0, min(H - 1, row_idx))
        points.append(row_idx)
    except:
        points.append(None)

for i in range(W):
    if points[i] is not None:
        screen_row = H - 1 - points[i]
        grid[screen_row][i] = '*'

for i in range(1, W):
    if points[i] is not None and points[i-1] is not None:
        row1 = H - 1 - points[i-1]
        row2 = H - 1 - points[i]
        col1 = i-1
        col2 = i
        
        if row1 != row2:
            min_row = min(row1, row2)
            max_row = max(row1, row2)
            for r in range(min_row, max_row + 1):
                grid[r][col1] = '*'
                grid[r][col2] = '*'
        else:
            grid[row1][col1] = '*'
            grid[row1][col2] = '*'

for x in range(W):
    star_positions = []
    for y in range(H):
        if grid[y][x] == '*':
            star_positions.append(y)
    
    if len(star_positions) == 1:
        y_pos = star_positions[0]
        if (x > 0 and grid[y_pos][x-1] == '*') or (x < W-1 and grid[y_pos][x+1] == '*'):
            pass
        else:
            if x > 0 and x < W-1:
                up_has = y_pos > 0 and grid[y_pos-1][x-1] == '*' and grid[y_pos-1][x+1] == '*'
                down_has = y_pos < H-1 and grid[y_pos+1][x-1] == '*' and grid[y_pos+1][x+1] == '*'
                if not (up_has or down_has):
                    grid[y_pos][x] = ' '
    elif len(star_positions) >= 2:
        min_y = min(star_positions)
        max_y = max(star_positions)
        for y in range(min_y + 1, max_y):
            grid[y][x] = '*'

for row in grid:
    print(''.join(row))

import sys
exec(sys.stdin.read())
