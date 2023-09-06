class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
    
    def ladrar(self):
        print("guau guau")

    def cumpleaños(self):
        self.edad += 1
        print(f"{self.nombre} está cumpliendo años hoy. Ahora tiene: {self.edad}")
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Raza: {self.raza}, Edad: {self.edad}"
    
snoopy = Perro("Snoopy", "beagle", 3)
print(snoopy)
snoopy.cumpleaños()
print(snoopy)
tommy = Perro("Tommy", "Golden", 2)

""" Ejercicio 3: Herencia (Nivel Intermedio) Crea una clase "PerroDeTrabajo" que herede de la clase "Perro". 
Esta nueva clase debe tener un campo adicional llamado "trabajo". Agrega un método "hacerTrabajo" que imprima en consola lo que hace el perro de trabajo (por ejemplo, "Buscando personas perdidas" para un perro de rescate). Crea un objeto de la clase PerroDeTrabajo y haz que haga su trabajo. 
"""

class PerroDeTrabajo(Perro):
    def __init__(self, nombre, raza, edad, trabajo):
        super().__init__(nombre, raza, edad)
        self.trabajo = trabajo

    def hacer_trabajo(self):
        print(f'{self.nombre} está haciendo su trabajo: {self.trabajo}')

perro_especialista = PerroDeTrabajo("Max", "pastor aleman", 5, "detectar armas")

print(perro_especialista)
perro_especialista.hacer_trabajo()





