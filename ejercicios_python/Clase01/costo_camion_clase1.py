"""
total = 0
precio = []
with open('/home/ailan/Python/ejercicios_python/Data/camion.csv', 'r') as archivo:
    lineas = archivo.read().splitlines()
    lineas.pop(0)
    for i in lineas:
        linea = i.split(',')
        precio.append([float(linea[1]) * float(linea[2])])
    for x in precio:
        total += sum(x)
print(total)
"""


def costo_camion(nombre_archivo):
    archivo = open('/home/ailan/Python/ejercicios_python/Data/camion.csv', 'rt')
    headers = next(archivo).split(',')
    total = 0
    precio = []
    for i in archivo:
        row=i.split(',')
        precio.append([float(row[1]) * float(row[2])])
    for x in precio:
        total += sum(x)
    print('Costo total: ', total)
    archivo.close()
costo = costo_camion('/home/ailan/Python/ejercicios_python/Data/camion.csv')


