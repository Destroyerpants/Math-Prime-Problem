import multiprocessing, sys, math

count = 0

inputs = []

data = []

primes = []
checkSet = [0,0]

block_size = 10
block_count = 1	

max_itterations = 20

def getPrimes():
	try:
		f = open('primes.txt', 'r')
		lines = f.readlines()
		for a in range(len(lines)):
			primes.append(int(lines[a]))
	except Exception as e: 
		print(e)

def getNextItem():
	x = checkSet[0]
	y = checkSet[1]
	xcoord = primes[x:x+1][0]
	ycoords = primes[y:y+block_size]
	
	checkSet[1] = checkSet[1] + block_size
	global block_count
	
	if checkSet[1] - block_size * block_count == 0:
		checkSet[1] = 0
		checkSet[0] = checkSet[0] + 1
		if checkSet[0] - block_size*block_count == 0:
			block_count = block_count + 1

	return (xcoord, ycoords)

def getInputs():
	for a in range(max_itterations):
		inputs.append(getNextItem())
	
def distanceFunction(x1, y1, x2, y2):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2) + math.sqrt((x1)**2 + (y1)**2)

def worker(args):
	x,ycoords = args
	for y in range(len(ycoords)):
		if x >= ycoords[y]:
			work(x,ycoords[y])

def work(x,y):
	smallest =  (1,1, distanceFunction(1,1,x,y))
	for i in range(1,x):
		for j in range(1,y):
			distance = distanceFunction(i,j,x,y)
			if distance < smallest[2]:
				smallest = (i, j , distance)
	global data
	data.append((x,y,smallest[0],smallest[1], smallest[2]))
	print(x,',',y,' x: ',smallest[0],' y: ', smallest[1],' delta: ',smallest[2])
	return

if __name__ == '__main__':
	jobs = []
	getPrimes()
	getInputs()
	print(inputs)
	for i in range(len(inputs)):
		p = multiprocessing.Process(target=worker, args=(inputs[i],))
		jobs.append(p)
		p.start()
		p.join()
	print(data)