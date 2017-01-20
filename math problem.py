import math
smallest =  (100, 100, 100000)
end = (int(input("X: ")),int(input("Y: ")))
for x in range(1,end[0]):
	for y in range(1,end[1]):
		distance = math.sqrt((x-end[0])**2 + (y-end[1])**2) + math.sqrt((x)**2 + (y)**2)
		if distance < smallest[2]:
			smallest = ( x, y , distance )
print(smallest)
input("Press Enter to exit")