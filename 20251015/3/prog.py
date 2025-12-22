import sys

data = sys.stdin.read().strip().split('\n')
if not data:
    sys.exit(0)

lns = data
h = len(lns)
w = len(lns[0])

g = 0
liq = 0
for i in range(1, h-1):
    for j in range(1, w-1):
        if lns[i][j] == '.':
            g += 1
        else:
            liq += 1

tot = g + liq

nw = h
nh = w
iw = nw - 2
ih = nh - 2

res = []
res.append('#' * nw)  

g_layers = g // iw
liq_layers = liq // iw

for i in range(ih):
    if i < g_layers:
        res.append('#' + '.' * iw + '#')
    else:
        res.append('#' + '~' * iw + '#')

res.append('#' * nw)  

for l in res:
    print(l)

mx = max(g, liq)
g_len = round(g * 20 / mx) if mx > 0 else 0
liq_len = round(liq * 20 / mx) if mx > 0 else 0

g_str = f"{g}/{tot}"
liq_str = f"{liq}/{tot}"
mx_len = max(len(g_str), len(liq_str))

print('.' * g_len + ' ' * (21 - g_len) + g_str.rjust(mx_len))
print('~' * liq_len + ' ' * (21 - liq_len) + liq_str.rjust(mx_len))
