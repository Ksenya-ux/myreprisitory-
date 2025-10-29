import itertools
def slide(seq, n):
    a = iter(seq)
    w = list(itertools.islice(a, n))
    
    while w:
        yield from w
        if len(w) < n:
            w.pop(0)
        else:
            w.pop(0)
            n_el = next(a, None)
            if n_el is not None:
                w.append(n_el)
