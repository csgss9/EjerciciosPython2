""" Ejercicio 4: Polimorfismo (Nivel Intermedio Alto) Crea una clase abstracta "Animal" con un método abstracto "hacerSonido". 
Haz que las clases "Perro" y "PerroDeTrabajo" hereden de "Animal" e implementen el método "hacerSonido". Crea una función que tome 
un objeto "Animal" como argumento e invoque el método "hacerSonido". Prueba la función con objetos de la clase Perro y PerroDeTrabajo.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_actividad(self):
        pass


class Perro(Animal):
    def hacer_actividad(self):
        return "jugando con la pelota"

class PerroDeTrabajo(Animal):
    def hacer_actividad(self):
        return "realizando trabajo"

def hacer_actividad_animal(animal):
    return animal.hacer_actividad()

perro = Perro()
perro_de_trabajo = PerroDeTrabajo()

print(hacer_actividad_animal(perro))
print(hacer_actividad_animal(perro_de_trabajo))