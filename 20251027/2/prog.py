import itertools
import sys

def slide(seq, n):
    it = iter(seq)
    window = list(itertools.islice(it, n))
    
    while window:
        yield from window
        if len(window) < n:
            window.pop(0)
        else:
            window.pop(0)
            next_item = next(it, None)
            if next_item is not None:
                window.append(next_item)

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    if input_data:
        exec(input_data)
