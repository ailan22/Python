#Ejercicio 2.9
import csv
archivo = open('../Data/camion.csv')
rows = csv.reader(archivo)
headers = next(rows)
for i in rows:    
    print(i)

archivo.close()
