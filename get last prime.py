fileHandle = open ( 'primes.txt',"r" )
lineList = fileHandle.readlines()
fileHandle.close()
print "The last line is:"
print lineList[-1]
input("Hit Enter to exit")