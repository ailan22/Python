#Ejercicio 4.5: Invertir una lista
def invertir_lista(lista):
    invertida = []
    for e in range(1, len(lista) + 1, 1):
        invertida.append(lista[-e])
    print(invertida)


invertir_lista([1, 2, 3, 4, 5])
invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])