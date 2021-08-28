import csv
# %% Ejercicio 3.18: Lectura de los árboles de un parque

def leer_parque(nombre_archivo, parque):
    with open(nombre_archivo, encoding="utf8") as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        arboles = []
        for i, row in enumerate(rows, start=1):
            if row[10] == parque:
                record = dict(zip(encabezados, row))
                arboles.append(record)
        return arboles


espacio_verde = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')


# %% Ejercicio 3.19: Determinar las especies en un parque

def especies(lista_arboles):
    especies = set()
    for i in lista_arboles:
        especies.add(i['nombre_com'])
    return especies


nombre_especies = especies(espacio_verde)