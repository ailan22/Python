# rebotes.py
# Archivo de ejemplo
# Ejercicio

altura = 100 #metros
veces_salta = 0

while veces_salta < 10:
    altura = altura * 3 / 5
    veces_salta = veces_salta + 1
    print(veces_salta, round(altura, 4))

print('Cantidad de saltos: ', veces_salta)
