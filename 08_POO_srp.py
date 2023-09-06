"""
Principios SOLID:

srp - principio de responsabilidad único: 
    Cada clasedebe tener una unica responsabilidad o tarea, independiente. Codigo mas facil
de mantener, legible y limpio.

"""

class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia/2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            print("Se movió el auto")
        else:
            print("Se necesita mas combustible")

    def obtener_posicion(self):
        return self.posicion

class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad    
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

tanque = TanqueDeCombustible()

auto = Auto(tanque)

print(auto.obtener_posicion())
auto.mover(10)
print(auto.obtener_posicion())
auto.mover(200)
print(auto.obtener_posicion())

