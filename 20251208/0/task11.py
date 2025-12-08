import asyncio
async  def prod(q1):
	for i in range(5):
		val = f"val={i}"
		await.q1.put(val)
		print(f"put {val} to queue 1")
		await asyncio.sleep(1)
async def mid(q1,q2):
	While 1:
		val = await q1.get()
		print(f"{val}")
		val = await q2.get()
		print(f"{val}")
async def cons(q2):	
	While 1:
	val = await q2.get()
