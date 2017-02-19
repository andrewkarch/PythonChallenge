import pprint, pickle, requests
baseURL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
r = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
with open("pickle.p", "w") as outFile:
	outFile.write(r.text)
with open("pickle.p", "r") as inFile:
	data1 = pickle.load(inFile)
	for data2 in data1:
		outString = ""
		for data in data2:
			outString += data[0] * data[1]
		print outString