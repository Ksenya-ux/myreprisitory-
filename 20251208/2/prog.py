import asyncio

async def w(q, d, e, i):
    await asyncio.sleep(d)
    c = 0
    while not e.is_set():
        await q.put(f"{c}_{d}")
        c += 1
        await asyncio.sleep(d)

async def s(a, b, t, e):
    while not e.is_set():
        x = asyncio.create_task(a.get())
        y = asyncio.create_task(b.get())
        d, p = await asyncio.wait([x, y], return_when=asyncio.FIRST_COMPLETED)
        for z in d:
            try:
                v = z.result()
                if v: await t.put(v)
            except: pass
        for z in p:
            z.cancel()

async def r(t, n, d, e):
    await asyncio.sleep(d)
    i = 0
    while i < n:
        print(await t.get())
        i += 1
        if i >= n:
            e.set()
            break
        await asyncio.sleep(d)

async def m():
    a, b, c, n = map(int, input().split(','))
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()
    t = asyncio.Queue()
    e = asyncio.Event()
    
    async with asyncio.TaskGroup() as g:
        g.create_task(w(q1, a, e, 1))
        g.create_task(w(q2, b, e, 2))
        g.create_task(s(q1, q2, t, e))
        g.create_task(r(t, n, c, e))
        while not e.is_set():
            await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(m())
