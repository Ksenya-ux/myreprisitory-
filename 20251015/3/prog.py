import sys

data_lines = []
for s in sys.stdin:
    t = s.rstrip()
    if t == '':
        break
    data_lines.append(t)

n_rows = len(data_lines)
n_cols = len(data_lines[0]) if n_rows > 0 else 0

left = 0
right = n_cols - 1

water_col = [0] * n_cols
air_col = [0] * n_cols

for line in data_lines[1:-1]:
    for idx in range(1, n_cols - 1):
        if line[idx] == '~':
            water_col[idx] += 1
        elif line[idx] == '.':
            air_col[idx] += 1

water_sum = sum(water_col)
air_sum = sum(air_col)
total_sum = water_sum + air_sum

new_w = n_rows
new_h = n_cols

result_matrix = [['#'] * new_w for _ in range(new_h)]

water_h = water_sum // (new_w - 2)
if water_sum % (new_w - 2) > 0:
    water_h += 1

for y in range(new_h):
    for x in range(new_w):
        if y == 0 or y == new_h - 1 or x == 0 or x == new_w - 1:
            continue
        if y >= new_h - 1 - water_h:
            result_matrix[y][x] = '~'
        else:
            result_matrix[y][x] = '.'

for row in result_matrix:
    print(''.join(row))

air_bar = round(20 * air_sum / total_sum) if total_sum > 0 else 0
water_bar = round(20 * water_sum / total_sum) if total_sum > 0 else 0

air_text = f' {air_sum}/{total_sum}'
water_text = f' {water_sum}/{total_sum}'

print('.' * air_bar + ' ' * (20 - air_bar) + air_text)
print('~' * water_bar + ' ' * (20 - water_bar) + water_text)
