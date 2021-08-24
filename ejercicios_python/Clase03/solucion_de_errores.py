#Ejercicio 3.1
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            print(True)
        else:
            print(False)
        i += 1

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

"""
fruta = 'La novela 1984 de George Orwell'
indice = 0
while indice < len(fruta):
    letra = fruta[indice]
    indice += 1
print(letra)
"""
