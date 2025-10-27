from itertoolsimport repeat
def repeater(seq,n):
	for i in seq:
		yield from repeat(i,n)
a = repeater([1,2,3],1)

	
