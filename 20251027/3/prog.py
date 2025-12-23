import itertools
import sys

if __name__ == "__main__":
    data = sys.stdin.read().strip()
    if data:
        n = int(data)
        print(*filter(lambda s: s.count('TOR') == 2, 
                     map(''.join, itertools.product('TOR', repeat=n))), 
              sep=', ')
