import asycio
async def  snd(x):
	evsnd.set()
async def mid(k):
	await envsd.wait()
	print('mid:mid envsd')
	if k== 0:
		evmid0.set()
	if k == 1:
		evmid1.set
async def rcv()
	await evmid0.wait()
	print('rcv:rcv evmid0')
	await evmid1.wait()
	print('rcv:rcv evmid1')
async def main():
	t1 = asyncio.create_task(rcv())
	t2 = asyncio.create_task(mid(1))
	t3 = asyncio.create_task(mid(0))
	t4 = asyncio.create_task(snd())
	await asyncio.gether(t1,t2,t3,t4)
asyncio.run(main)

