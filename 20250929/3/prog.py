import sys

data = []
try:
    while True:
        text = input()
        if text == "":
            break
        data.append(text.strip())
except EOFError:
    pass

if not data:
    import sys
    data = [line.strip() for line in sys.stdin if line.strip()]

size = len(data) // 2

first_matrix = []
second_matrix = []

for idx in range(size):
    first_matrix.append(list(map(int, data[idx].split(','))))
    second_matrix.append(list(map(int, data[idx + size].split(','))))

output = []
for i in range(size):
    current_row = []
    for j in range(size):
        total = 0
        for k in range(size):
            total += first_matrix[i][k] * second_matrix[k][j]
        current_row.append(str(total))
    output.append(','.join(current_row))

for row in output:
    print(row)
