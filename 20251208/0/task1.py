 import asyncio
 async def  squarer(x):
	await asyncio.sleep(0)
	return x*x
 async def  doubler(x):
	await asycio.sleep(0)
	return x*2
async def main(x,y):
	async with acyncio.TaskGroup() as tg:
		sx = tg.create_task(squarer(x))
		sy = tg.create_task(squarer(y))
	x, y = sx.result(), sy.result()
	async with acyncio.TaskGroup() as tg:
		dx = tg.create_task(doubler(x))
		dy = tg.create_task(doubler(y))
	x, y = dx.result(), dy.result()
	print([x,y])
