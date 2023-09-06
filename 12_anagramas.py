# palabra1 = input("Ingrese la 1era palabra: ")
# palabra2 = input("Ingrese la 2da palabra: ")



# def anagrama_valido(palabra1, palabra2):
#     if len(palabra1) == len(palabra2):
#         for letter in palabra1:
#             if letter not in palabra2:
#                 return("no son anagramas")
#         return("son anagramas")
#     else:
#         return("No son anagramas")
    
# print(f"Sus palabras: {anagrama_valido(palabra1, palabra2)}")

#--------------------------------------------------------------------------------------------------------
#Otra manera

# from collections import Counter  #Cuenta los elementos de una colección

# def anagrama_valido(palabra1, palabra2):
#     c_palabra1 = Counter(palabra1)
#     c_palabra2 = Counter(palabra2)
#     if c_palabra1 == c_palabra2:
#         print("son anagramas")
#     else:
#         print("No son anagramas")

# anagrama_valido("zara", "raza")

""" salida: diccionario que tiene como valor el n° de veces que aparece la letra en la palabra 
Counter({'a': 2, 'z': 1, 'r': 1}) Counter({'a': 2, 'r': 1, 'z': 1}) """

#------------------------------------------------------------------------------------------------------
#Otra manera:

palabra1 = input("Ingrese la 1era palabra: ")
palabra2 = input("Ingrese la 2da palabra: ")

def anagrama_valido(palabra1,palabra2):
    palabra1 = sorted(palabra1)
    palabra2 = sorted(palabra2)
    if palabra1 == palabra2:
        print("son anagramas")
    else:
        print("no son anagramas")

anagrama_valido(palabra1, palabra2)