import pickle 
pickle.dumps([1,2,3,45,5])
p = pickle.dumps([1,2,3,4,5])
print(p,type(p))
with open('file4','bw+') as f:
	pickle.dump(('Привет',42,b'HeLLo'), f, protocol=0)
	
