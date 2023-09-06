"""
Calcular la suma de los primeros N numeros primos
"""
import time 
from math import sqrt,floor

def es_primo(n):
   #for divisor in range(2, n): # para 50000 Tarda: 8.23708462715149 segundos
    for divisor in range(2, floor(sqrt(n)) + 1):    #para 50000 Tarda: 0.08249950408935547 segundos
        if n % divisor == 0:
            return False
    return True

desde = time.time()
for n in range(1, 10):
    print(n, es_primo(n))

hasta = time.time()

print(f'Tarda: {hasta - desde} segundos')


def sumar_primos(n):
    suma = 0
    numero = 0
    contador = 0
    while contador < n:
        numero += 1
        if es_primo(numero):
            contador += 1
            suma += numero
    return suma

print(sumar_primos(200))
