def count_airports(file_name):
	SMALL_AIRPORTS = 0
	LARGE_AIRPORTS = 0
	file = open(file = file_name, mode = 'rt', encoding = 'utf-8')
	line = file.readline()
	list = []
	while line:
		line = line.replace("\"","")
		data = line.split(",")
		if data[2] == "small_airport":
			SMALL_AIRPORTS  = SMALL_AIRPORTS  + 1
		elif data[2] == "large_airport":
			LARGE_AIRPORTS = LARGE_AIRPORTS + 1
		else:
			pass
		line = file.readline()

	print(LARGE_AIRPORTS)
	print(SMALL_AIRPORTS)

count_airports('c:/airports.csv')
	