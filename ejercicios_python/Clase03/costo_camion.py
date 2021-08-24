#Ejercicio 3.9
def costo_camion(archivo):
    import csv
    with open (archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        print(encabezados)
        total = []
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
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
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        print(f'COSTO TOTAL: {round(suma, 2)}')
costo_camion('../Data/fecha_camion.csv')