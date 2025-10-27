def walk2d():
	while True:
		dx = 0
		dy = 0
		x1 = yield  dx
		y1 = yield  dy
		yield (next(x1) - x1)/(next(y1) - y1)
		dy += 1
		dx += 1
ans = walk2d()
