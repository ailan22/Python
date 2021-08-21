#Ejercicio 2.10
import csv
import sys
def costo_camion(archivo):
    with open(archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        total = []
        for i in f:
            try:
                linea = i.split(',')
                costo_producto = (int(linea[1]) * float(linea[2]))
                total.append(costo_producto)
                suma_total = 0
                for elemento in total:
                    suma_total += elemento
                print('Costo total por producto', round(costo_producto, 2))
            except ValueError:
                print('Falta un valor')
    print('COSTO TOTAL', suma_total)
if len (sys.argv) == 2:
    archivo = sys.argv[1]
else:
    archivo = '../Data/camion.csv'

costo_total = costo_camion('../Data/camion.csv')
