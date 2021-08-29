#Ejercicio 4.3: Búsquedas de un elemento
def buscar_u_elemento(lista, i):
    pos = -1
    for y, elem in enumerate(lista):
        if elem == i:
            pos = y
    return pos

buscar_u_elemento([1,2,3,2,3,4],3)
buscar_u_elemento([1,2,3,2,3,4],2)
buscar_u_elemento([1,2,3,2,3,4],3)
buscar_u_elemento([1,2,3,2,3,4],5)

def buscar_n_elemento(lista, i):
    cont = 0
    pos = -1
    for y, elem in enumerate(lista):
        if elem == i:
            pos = y
            cont += 1
    return 'Posición: ', pos, 'Cantidad de veces repetidas: ', cont

buscar_n_elemento([1,2,3,2,3,4],3)
buscar_n_elemento([1,2,3,2,3,4],2)
buscar_n_elemento([1,2,3,2,3,4],3)
buscar_n_elemento([1,2,3,2,3,4],5)


#Ejercicio 4.4: Búsqueda de máximo y mínimo
def maximo(lista):
    max_value = 0
    for num in lista:
        if (max_value is None or num > max_value):
            max_value = num
    return max_value

maximo([1,2,7,2,3,4])

def minimo(lista):
    min_value = lista[0]
    for num in lista:
        if num < min_value:
            min_value = num
    return min_value

minimo([1,2,7,2,3,4])
