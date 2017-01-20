array = []
fixed = []
try:
	f = open("primes.txt",'r')
	for l in f:	array.append(int(l))
		
	for a in range(len(array)-1):
		if array[a] != array[a+1]:
			fixed.append(array[a])
	
	f.close()
	
	f = open("primes.txt", "w")
	for a in fixed:
		f.write(str(a) + "\n")
	f.close()
except Exception as e: 
	print str(e)
	