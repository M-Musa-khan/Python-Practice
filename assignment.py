def color_listtodict(colorlist):
	blue = 0
	green = 0	

	for x in colorlist:
		if x is "blue":
			blue += 1
		elif x is "green":
			green += 1
	
	colordict = { "blue":blue, "green":green}	

	return colordict

mylist = ["blue","green","blue","green","green","blue","blue"]

print(color_listtodict(mylist))
