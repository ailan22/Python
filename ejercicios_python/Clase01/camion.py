f = open('/home/ailan/Python/ejercicios_python/Data/camion.csv', 'rt')
headers = next(f).split(',')
#print(headers)
for line in f:
    row = line.split(',')
    print(row)
f.close()
