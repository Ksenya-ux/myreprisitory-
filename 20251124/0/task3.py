import struct, random, system
st = struct.pack('!3sfi', b'Hel', 0.5, 1)
print(*struct.unpack('!3sfi',st))
seq = [(random.random(), bytes(random.sample(range(5),3)), random.randange(10000)) i for i in range(10)]
with open(sys.argv[1],'bw+') as fout:
	for t in seq:
		w = fout.write(struct.pack('f3si',*t))
with open(sys.argv[1],'br') as fin:
	with open(sys.argv[2],'bw+') as fout:
		size = struct.calcsizw('f3si')
		while s:= fin.rwad(size):
			w = fout.write(struct.pack('f3si',*struct.unpack(!3sfi',st))


