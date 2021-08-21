#Ejercicio 2.7: Buscar precios
import csv
def buscar_precio():
    with open('../Data/precios.csv') as archivo:
        rows = csv.reader(archivo)
        headers = next(rows)
        headers
        producto = input('Ingrese el producto: ')
        for i in rows:
            try:
                if(producto == i[0]):
                    print('El precio de un cajón de', producto, 'es: ', i[1])
                    break
            except:
                print(producto, 'no figura en el listado de precios.')
buscar_precio()