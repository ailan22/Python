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
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo = [ncajones * precio for s in record]
        print(costo)
#            try:
#                ncajones = int(record['cajones'])
#                precio = float(record['precio'])
#                costo_total = ncajones * precio
#                total.append(costo_total)
#                print(list(record.values()))
#                #calculo el total
#                suma = 0
#                for elemento in total:
#                    suma += elemento
#            # Esto atrapa errores en los int() y float() de arriba.
#            except ValueError:
#                print(f'Fila {num_fila}: No pude interpretar: {fila}')
#        print(f'COSTO TOTAL: {round(suma, 2)}')
costo_camion('../Data/fecha_camion.csv')