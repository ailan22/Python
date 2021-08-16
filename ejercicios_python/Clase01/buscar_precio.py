import csv
def buscar_precio():
    with open('../Data/precios.csv') as f:
        rows = csv.reader(f)
        producto = input('Ingrese el producto: ')
        for row in rows:
            try:
                if(producto == row[0]):
                    print(f'El precio de un cajón de {producto} es: ', row[1])
                    break
            except:
                print(f'{producto} no figura en el listado de precios.')
buscar_precio()
