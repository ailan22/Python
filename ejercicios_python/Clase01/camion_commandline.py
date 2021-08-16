#Ejercicio 2.10
"""
import csv
archivo = open('../Data/camion.csv')
rows = csv.reader(archivo)
headers = next(rows)
for i in rows:
    print(i)

archivo.close()
"""
import csv
import sys
def costo_camion (archivo):
    with open(archivo, 'rt') as archivo:
        rows = csv.reader(archivo)
        headers = next(rows)
        precios = []
        for i in archivo:
            row = i.split(',')
            cajones = int(row[1])
            precio = float(row[2])
            precios.append([float(row[1]) * float(row[2])])
            print(precios)
            suma = 0
        for elemento in precios:
            suma += elemento
            print('costo total: ', suma)
        else:
            print('Cantidad de cajones vacías')
if len (sys.argv) == 2:
    archivo = sys.argv[1]
else:
    archivo = '../Data/missing.csv'
costo_camion('../Data/missing.csv')