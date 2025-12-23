def gen_fib(start, count):
    seq = [1, 1]
    for idx in range(2, start + count):
        if idx >= start:
            yield seq[idx-1] + seq[idx-2]
        seq.append(seq[idx-2] + seq[idx-1])

import sys
exec(sys.stdin.read())
