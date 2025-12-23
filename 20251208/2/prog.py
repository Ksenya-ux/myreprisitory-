import asyncio
import random
import math

async def merge(A1, A2, start, middle, finish, event_in1, event_in2, event_out):
    """Слияние двух отсортированных отрезков"""
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

async def copy_segment(A1, A2, start, finish, event_in, event_out):
    """Копирование отрезка"""
    await event_in.wait()
    for i in range(start, finish):
        A2[i] = A1[i]
    event_out.set()

async def mtasks(A):
    """Планирование задач сортировки слиянием - асинхронная, но не запускает задачи"""
    n = len(A)
    
    if n <= 1:
        return [], A[:]
    
    # Создаем рабочие массивы
    Awork = A[:]  # Рабочая копия A
    B = [0] * n   # Вспомогательный массив (будет результатом)
    
    tasks = []
    
    # Определяем количество уровней
    levels = math.ceil(math.log2(n)) if n > 1 else 0
    
    # Определяем начальные src и dst
    # Если нечетное количество уровней, начинаем с Awork->B
    # Иначе начинаем с B->Awork (но сначала копируем Awork в B)
    if levels % 2 == 1:
        src, dst = Awork, B
    else:
        src, dst = B, Awork
        # Копируем Awork в B для начала
        B[:] = Awork[:]
    
    # Создаем события для единичных блоков
    block_size = 1
    blocks = n
    events = [asyncio.Event() for _ in range(blocks)]
    for ev in events:
        ev.set()  # Единичные блоки уже "отсортированы"
    
    # Основной цикл по уровням
    while block_size < n:
        new_events = []
        new_blocks = (n + 2 * block_size - 1) // (2 * block_size)
        
        for block in range(0, blocks, 2):
            start = block * block_size
            middle = min(start + block_size, n)
            finish = min(start + 2 * block_size, n)
            
            ev_out = asyncio.Event()
            new_events.append(ev_out)
            
            if block + 1 < blocks:
                # Есть два блока для слияния - создаем корутину
                task = merge(src, dst, start, middle, finish,
                            events[block], events[block + 1], ev_out)
            else:
                # Только один блок (нечетное количество) - просто копируем
                task = copy_segment(src, dst, start, finish,
                                   events[block], ev_out)
            
            tasks.append(task)
        
        # Обновляем для следующего уровня
        events = new_events
        blocks = new_blocks
        src, dst = dst, src
        block_size *= 2
    
    return tasks, B

import sys
exec(sys.stdin.read())

