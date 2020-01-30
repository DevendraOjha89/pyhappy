file = open(file='c:/airports.csv', mode ='rt', encoding = 'utf-8')
line = file.readline()

while line:
	split_line = line.split(',')
	for data in split_line:
		print(data)
	line = file.readline()
