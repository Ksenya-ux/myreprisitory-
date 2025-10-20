al = input().split()
def s(al):
	d = {}
	for i in al:
		d[i] = d.setdefault(i,0) + 1
	return al
