
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]
"""
from collections import Counter
total_cajones = Counter()
for nombre, n_cajones, precio in camion:
        total_cajones[nombre] += n_cajones

print(total_cajones['Naranja'])
"""
#Ejercicio 3.9
def costo_camion(archivo):
    import csv
    with open (archivo, 'rt') as f:
        filas = csv.reader(f)
        headers = next(filas)
        print(headers)
        total = []
        for num_fila, fila in enumerate(filas, start=1):
            record = dict(zip(headers, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total = ncajones * precio
                total.append(costo_total)
                print(list(record.values()))
                #calculo el total
                suma = 0
                for elemento in total:
                    suma += elemento
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {num_fila}: No pude interpretar: {fila}')
        print(f'COSTO TOTAL: {round(suma, 2)}')
costo_camion('../Data/fecha_camion.csv')

#camion = costo_camion('../Data/camion.csv')
from collections import Counter
tenencias = Counter()
for s in camion:
    tenencias[s['nombre']] += s['cajones']

print(tenencias['Naranja'])
