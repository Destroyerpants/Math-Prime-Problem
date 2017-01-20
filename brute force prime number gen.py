import os
path =  os.getcwd() + "\primes.txt"

curr = 3
try:
	f = open("primes.txt", 'r')
	lines = f.readlines()
	f.close()
	curr = int(lines[-1]) + 2
	f.close()
except:
	pass

while True:
	f = open( "primes.txt", 'a')
	count = 25
	while count > 0:
		prime = True
		for x in range(2,curr):
			if curr % x == 0: 
				prime = False
				
		if prime:
			f.write(str(curr) + "\n")
		curr = curr + 2
		count = count-1
	f.close()
	print("Writing to file: " + str(os.path.getsize(path)) + " bytes" ) 