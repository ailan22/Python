#Ejercicio 2.14
lista = ['banana', 'manzana', 'mandarina']

def geringoso():
    diccionary = {}
    cadena = ''
    for s in lista:
        cont = 0
        for letra in s:
            cadena += letra
            if letra in 'aeiou':
                cadena += 'p' + letra
        diccionary[s] = cadena
        cadena = ''
        cont += 1
    return diccionary

diccionary = geringoso()
print(diccionary)
