import itertools; print(*filter(lambda s: s.count('TOR') == 2, map(''.join, itertools.product('TOR', repeat=int(input())))), sep=', ')

