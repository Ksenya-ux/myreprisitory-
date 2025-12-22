import asyncio

stop = asyncio.Event()
stack_ping = asyncio.Event()

async def writer(q, delay):
    i = 0
    while True:
        await asyncio.sleep(delay)
        if stop.is_set():
            return
        s = f"{i}_{delay}"
        await q.put(s)
        i += 1

async def stacker(q, stack):
    while True:
        if stop.is_set():
            return
        got = asyncio.create_task(q.get())
        die = asyncio.create_task(stop.wait())
        done, pending = await asyncio.wait({got, die}, return_when=asyncio.FIRST_COMPLETED)

        for t in pending:
            t.cancel()

        if die in done:
            return

        val = got.result()
        stack.append(val)
        stack_ping.set()

async def reader(stack, cnt, delay):
    for _ in range(cnt):
        await asyncio.sleep(delay)

        while not stack:
            if stop.is_set():
                return
            stack_ping.clear()
            await stack_ping.wait()

        print(stack.pop())

    stop.set()
    return

async def main():
    delay1, delay2, delay3, count = [int(x.strip()) for x in input().split(",")]
    q = asyncio.Queue()
    st = []

    t1 = asyncio.create_task(writer(q, delay1))
    t2 = asyncio.create_task(writer(q, delay2))
    t3 = asyncio.create_task(stacker(q, st))
    t4 = asyncio.create_task(reader(st, count, delay3))

    await t4
    await asyncio.gather(t1, t2, t3, return_exceptions=True)

asyncio.run(main())

import sys
exec(sys.stdin.read())
