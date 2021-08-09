#gerigonso.py
#Ejercicio gerigonso

cadena = 'gerigonso'
letras = ''
capadepenapa = ''
longitud = list(range(0, len(cadena)))
for i in longitud:
    letras = cadena[i]
    if letras == 'a':
        capadepenapa += letras.replace('a', 'apa')
    elif letras == 'e':
        capadepenapa += letras.replace('e', 'epe')
    elif letras == 'i':
        capadepenapa += letras.replace('i', 'ipi')
    elif letras == 'o':
        capadepenapa += letras.replace('o', 'opo')
    elif letras == 'u':
        capadepenapa += letras.replace('u', 'upu')
    else:
        capadepenapa += letras

print(capadepenapa)
