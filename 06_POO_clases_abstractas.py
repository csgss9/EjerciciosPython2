from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, name, actividad):
        self.name = name
        self.actividad = actividad
    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def __str__(self):
        return f'Soy {self.name} y soy {self.actividad} y estoy {self.hacer_actividad()}'

class Estudiante(Persona):
    def __init__(self,name,actividad):
        super().__init__(name,actividad)
    
    def hacer_actividad(self):
       # print("estudiando...")
        return "estudiando..."

class Cantante(Persona):
    def __init__(self,name,actividad):
        super().__init__(name,actividad)

    def hacer_actividad(self):
        #print("cantando...")
        return "cantando..."
pablo = Cantante("Pablo","cantante")
luis = Estudiante("Luis", "Estudiante")

print(pablo)
print(pablo.hacer_actividad())
print(luis)
print(luis.hacer_actividad())
