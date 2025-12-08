 import asyncio
 async def  squarer(x):
	await asyncio.sleep(0)
	await asyncio.sleep(0)
	return x*x
 async def  doubler(x):
	await asycio.sleep(0)
	return x*2
async def main(x, y):
	x,y = await asyncio.gather(squarer(x), squarer(y))
	x,y = await asyncio.gather(doubler(x), doubler(y))
	print([x,y])
