import asyncio
import sys
from math import log2

async def merge(A1, A2, s, m, f, e1, e2, eo):
    await e1.wait()
    await e2.wait()
    i, j, k = s, m, s
    while i < m and j < f:
        if A1[i] <= A1[j]:
            A2[k] = A1[i]
            i += 1
        else:
            A2[k] = A1[j]
            j += 1
        k += 1
    while i < m:
        A2[k] = A1[i]
        i += 1
        k += 1
    while j < f:
        A2[k] = A1[j]
        j += 1
        k += 1
    eo.set()

async def mtasks(A):
    n = len(A)
    if n <= 1:
        return [], A[:]
    
    B = [0] * n
    ts = []
    sev = []
    for _ in range((n + 1) // 1):
        e = asyncio.Event()
        e.set()
        sev.append(e)
    
    l = 1
    src, dst = A, B
    
    while l < n:
        tev = []
        for s in range(0, n, 2 * l):
            m = min(s + l, n)
            f = min(s + 2 * l, n)
            if m >= f:
                for i in range(s, f):
                    dst[i] = src[i]
                e = asyncio.Event()
                e.set()
                tev.append(e)
                continue
            eo = asyncio.Event()
            tev.append(eo)
            i1 = s // l
            i2 = m // l
            e1 = sev[i1] if i1 < len(sev) else asyncio.Event()
            e2 = sev[i2] if i2 < len(sev) else asyncio.Event()
            if isinstance(e1, list):
                e1 = e1[0] if e1 else asyncio.Event()
            if isinstance(e2, list):
                e2 = e2[0] if e2 else asyncio.Event()
            t = merge(src, dst, s, m, f, e1, e2, eo)
            ts.append(t)
        src, dst = dst, src
        sev = tev
        l *= 2
    
    return ts, src

if __name__ == "__main__":
    exec(sys.stdin.read())
