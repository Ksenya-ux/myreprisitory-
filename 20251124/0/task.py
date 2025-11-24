import sys
with open(sys.argv[1], 'br') as input_file:
	bins = input_file.read()
	with opend(sys.argv[1],'wb') as fout:
		print(bins)
		fout.write(bins[len(bins)//2:] + bins[:len(bins)//2])
		
