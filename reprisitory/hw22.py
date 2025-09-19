import sys
filename = sys.argv[1]
try:
	with open(filename, 'r') as f:
		a = f.read().strip()
except FileNotFoundError:
		print(f"Error:Filr {filename} not found")
a = a.split(',')
output_file = str(filename)[:-2] +'out'
with open(output_file,"w") as f_out:
	results = ','.join(map(str,a))+'\n'
	f_out.write(results)


