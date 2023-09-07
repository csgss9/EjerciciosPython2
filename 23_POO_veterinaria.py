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
        self.especialidad = especialidad
        self.citas = []

    def atender_cita(self, cita):
        pass

    def registrar_diagnostico(self, diagnostico):
        pass

class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.mascota = []

    def agendar_cita(self): 
        pass

class Cita:
    def __init__(self, fecha, motivo):
        self.fecha = fecha
        self.motivo = motivo

class Diagnostico:
    def __init__(self, fecha, descripcion):
        self.fecha = fecha
        self.descripcion = descripcion

    def registrar_diagnostico(self):
        pass

    def mostrar_diagnostico(self):
        pass