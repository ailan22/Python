"""
a = [1, 2, 3, 4, 5]
print([2*x for x in a])

nombres = ['Edmundo', 'Juana']
print([nom.upper() for nom in nombres])

c = [1, -5, 4, 2, -2, 10]
d = [2*x for x in a if x > 0]
print(d)
"""

import csv
f = open('../Data/camion.csv')
row = csv.reader(f)
headers = next(f)
for line in row:
    print(line)


