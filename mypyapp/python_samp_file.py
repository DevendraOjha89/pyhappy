file = open(file='c:/airports.csv', mode='rt', encoding='utf-8')
print(file)
line = file.readline()

while line:
   print(line)
   line = file.readline()
