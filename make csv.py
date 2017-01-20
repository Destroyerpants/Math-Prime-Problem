import multiprocessing as mp
import math

checkSet = [0,0]
todo = []
primes = []
data = []
block_size = 4
block_count = 1	
max_itterations = 10000

def getPrimes():
	try:
		f = open('primes.txt', 'r')
		lines = f.readlines()
		for a in range(len(lines)):
			primes.append(int(lines[a]))
	except Exception as e: 
		print str(e)

def mathProblem(x, y):
	smallest =  (100, 100, sys.maxint)
	end = (input("X: "),input("Y: "))
	for x in range(1,end[0]):
		for y in range(1,end[1]):
			distance = math.sqrt((x-end[0])**2 + (y-end[1])**2) + math.sqrt((x)**2 + (y)**2)
			if distance < smallest[2]:
				smallest = ( x, y , distance )
	return smallest
	
def worker((xcoord,ycoords)):
	for y in range(len(ycoords)):
		if xcoord - y >=0:
			data[xcoord].append(mathProblem(xcoord,ycoords[y]))
	
def getNextItem():
	x = checkSet[1]
	y = checkSet[0]
	xcoord = primes[x:x+1][0]
	ycoords = primes[y:y+block_size]
	
	checkSet[0] = checkSet[0] + 1

	global block_count
	
	if checkSet[0] - block_size * block_count == 0:
		checkSet[0] = 0
		checkSet[1] = checkSet[1] + 1
		if checkSet[1] - block_size*block_count == block_size:
			block_count = block_count + 1

	return (xcoord, ycoords)

def getToDoList():
	for a in range(max_itterations):
		todo.append(getNextItem)
	
if __name__ == '__main__':
	getPrimes()
	getToDoList()
	p = mp.Pool(mp.cpu_count())
	map(worker, todo)