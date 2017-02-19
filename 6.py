x = 1
nextFile = "90052"
while x <= 910:
	with open("channel/"+nextFile+".txt", "r") as inFile:
		nextFile = inFile.read()
		nextFile = nextFile[nextFile.rfind(' ')+1:]
		print nextFile
		#with open(nextFile+".txt", "r"):

	#print str(x) + " " + r.text
	#x+=1 