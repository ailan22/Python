"""
def add(x, y):
    assert isinstance(x, int), 'Necesito un entero (int)'
    assert isinstance(y, int), 'Necesito un entero (int)'
    return x + y

print(add(2, 'f'))
"""
import types

"""
def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento
        i = i-1
        invertida.append (lista.pop(i))  #
    return invertida

l = [1, 2, 3, 4, 5]
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')
"""
"""
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    registro = {}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
"""
"""
def busqueda_con_index(lista, e):
    '''Busca un elemento e en la lista.

    Si e está en lista devuelve el índice,
    de lo contrario devuelve -1.
    '''
    if e in lista:
        print(f'El numero es: {lista.index(e)} ')
        return True
    else:
        print(-1)
        return False

busqueda_con_index([1, 4, 54, 3, 0, -1], 1)
"""
"""
def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    print(i)
    print(pos)

busqueda_lineal([1, 4, 54, 3, 0, -1], 4)

"""
"""
import csv
f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
for num_fila, fila in enumerate(rows, start=1):
    record = dict(zip(headers, fila))
    print(record)
#for line in rows:
#    r = list(zip(types, row))
#    print(r)
"""
import csv
f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(headers)

def fecha_a_tupla(headers):
    indexs = [] #creo una lista donde almaceno las posiciones de "/"
    i=0
    while i<len(f):
        if f[i] == "/": #"Itero entre la fecha para almacenar las posiciones de "/"
            indexs.append(i)
        i=i+1
    new_fecha = (int(headers[:indexs[0]]),int(headers[indexs[0]+1:indexs[1]]),int(headers[indexs[1]+1:])) #Almaceno en tupla la fecha sin "/"
    print(new_fecha)

fecha_a_tupla(headers)