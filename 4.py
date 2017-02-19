import requests
baseURL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
r = requests.get(baseURL+"12345")
x = 1
while x <= 400:
	nextURL = r.text[r.text.rfind(' ')+1:]
	r = requests.get(baseURL+nextURL)
	print str(x) + " " + r.text
	x+=1 