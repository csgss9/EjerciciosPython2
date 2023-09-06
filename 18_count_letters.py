#implementar la lógica de una función que cuente la cantidad de ocurrencias de cada letra en una cadena de texto y lo almacene en un diccionario.


def count_letters(frase):
    diccionario = {}
    for letra in frase:
        if letra in diccionario:
            diccionario[letra] += 1
        else: 
            diccionario[letra] = 1
    return diccionario

print(count_letters("Hola Mundo"))