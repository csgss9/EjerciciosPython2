class Mascota:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

class Perro(Mascota):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.raza = raza
    
class Gato(Mascota):
    def __init__(self, nombre, edad, peso, color_pelaje):
        super().__init__(nombre, edad, peso)
        self.color_pelaje = color_pelaje


class Ave(Mascota):
    def __init__(self, nombre, edad, peso, especie):
        super().__init__(nombre, edad, peso)
        self.especie = especie

class Veterinario:
    def __init__(self, nombre, especialidad, citas):
        self.nombre = nombre
        self.especialidad = 
        self.citas = []

class Cliente:
    pass

class Cita:
    pass
class Diagnostico:
    pass