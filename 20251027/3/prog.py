import itertools as it; print(*sorted(filter(lambda s: s.count('TOR')==2, map(''.join, it.product('TOR', repeat=int(input()))))), sep=', ')
