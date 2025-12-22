import asyncio
import sys
import random

stop = asyncio.Event()
stack_ping = asyncio.Event()

async def writer(q, delay, e):
    i = 0
    while not e.is_set():
        await q.put(f"{i}_{delay}")
        i += 1
        await asyncio.sleep(delay)

async def stacker(q, stack, e):
    while not e.is_set():
        try:
            item = await asyncio.wait_for(q.get(), timeout=0.1)
            stack.append(item)
            stack_ping.set()
        except asyncio.TimeoutError:
            continue
        except asyncio.CancelledError:
            break

async def reader(stack, n, delay, e):
    await asyncio.sleep(delay)
    for i in range(n):
        while not stack:
            if e.is_set():
                return
            stack_ping.clear()
            await stack_ping.wait()
        
        print(stack.pop())
        
        if i < n - 1:
            await asyncio.sleep(delay)
    
    e.set()

async def main():
    delay1, delay2, delay3, count = map(int, input().split(','))
    q = asyncio.Queue()
    stack = []
    stop_event = asyncio.Event()
    
    writer1_task = asyncio.create_task(writer(q, delay1, stop_event))
    writer2_task = asyncio.create_task(writer(q, delay2, stop_event))
    stacker_task = asyncio.create_task(stacker(q, stack, stop_event))
    reader_task = asyncio.create_task(reader(stack, count, delay3, stop_event))
    
    await reader_task
    
    writer1_task.cancel()
    writer2_task.cancel()
    stacker_task.cancel()
    
    await asyncio.gather(
        writer1_task, 
        writer2_task, 
        stacker_task, 
        return_exceptions=True
    )

async def merge(A1, A2, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    await event_in2.wait()

    i, j, k = start, middle, start
    while i < middle and j < finish:
        if A1[i] <= A1[j]:
            A2[k] = A1[i]
            i += 1
        else:
            A2[k] = A1[j]
            j += 1
        k += 1

    while i < middle:
        A2[k] = A1[i]
        i += 1
        k += 1

    while j < finish:
        A2[k] = A1[j]
        j += 1
        k += 1

    event_out.set()

async def mtasks(A):
    n = len(A)

    Awork = list(A)
    B = [None] * n

    tasks = []
    if n <= 1:
        return tasks, Awork

    events = []
    for start in range(0, n, 1):
        e = asyncio.Event()
        e.set()
        events.append(e)

    empty_ready = asyncio.Event()
    empty_ready.set()

    src, dst = Awork, B
    size = 1

    while size < n:
        new_events = []
        run_len = 2 * size

        run_index = 0
        for start in range(0, n, run_len):
            middle = min(start + size, n)
            finish = min(start + run_len, n)

            left_event = events[run_index]
            run_index += 1

            if middle < finish:
                right_event = events[run_index]
                run_index += 1
            else:
                right_event = empty_ready

            out_event = asyncio.Event()
            new_events.append(out_event)

            tasks.append(
                merge(src, dst, start, middle, finish,
                      left_event, right_event, out_event)
            )

        src, dst = dst, src
        events = new_events
        size *= 2

    return tasks, src

asyncio.run(main())
