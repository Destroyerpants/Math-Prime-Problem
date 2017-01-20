import multiprocessing, sys, math
inputs = [(3,3), (3,5), (3,7), (3,9), (5,3), (5,5), (5,7)]
data = []
def distanceFunction(x1, y1, x2, y2):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2) + math.sqrt((x1)**2 + (y1)**2)

def worker(num):
	x,y = num
	smallest =  (1,1, distanceFunction(1,1,x,y))
	for i in range(1,x):
		for j in range(1,y):
			distance = distanceFunction(i,j,x,y)
			if distance < smallest[2]:
				smallest = (i, j , distance)
	data.append((x,y,smallest))
	print('(x,y): ',x,',',y,' x: ',smallest[0],' y: ', smallest[1],' delta: ',smallest[2])
	return

if __name__ == '__main__':
	jobs = []
	for i in range(len(inputs)):
		p = multiprocessing.Process(target=worker, args=(inputs[i],))
		jobs.append(p)
		p.start()