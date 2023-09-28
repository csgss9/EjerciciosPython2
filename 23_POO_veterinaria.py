class Mascota:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.citas = []

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
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.citas = []
        self.diagnosticos = []

    def registrar_cita(self, cita):
        self.citas.append(cita)

    def lista_de_citas(self):
        citas_info = [f"Cita {i + 1}: ({cita.fecha}, '{cita.motivo}')" for i, cita in enumerate(self.citas)]
        return ", ".join(citas_info)
    
    def registrar_diagnostico(self, mascota, fecha, descripcion):
        nuevo_diagnostico = Diagnostico(fecha, mascota, descripcion)
        self.diagnosticos.append(nuevo_diagnostico)
    
    def mostrar_diagnostico(self):
        return self.diagnosticos
class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.mascotas = []

    def agendar_cita(self, cita, mascota, veterinario): 
        print("Agendando cita...")
        mascota.citas.append(cita)
        cita.veterinario = veterinario

    
    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)
    
    def ver_lista_de_mascotas(self):
        return self.mascotas
    
    
        
class Cita:
    def __init__(self, fecha, motivo, veterinario, mascota):
        self.fecha = fecha
        self.motivo = motivo
        self.veterinario = veterinario
        self.mascota = mascota

    def __str__(self):
        return f"Cita agendadada: \n Mascota: {self.mascota.nombre} \n Veterinario: {self.veterinario.nombre} - {self.veterinario.especialidad} \n Fecha: {self.fecha} \n Motivo: {self.motivo}"

class Diagnostico:
    def __init__(self, fecha, mascota, descripcion):
        self.fecha = fecha
        self.descripcion = descripcion
        self.mascota = mascota
        
    def __str__(self):
        return f"Diagnóstico para {self.mascota.nombre}:\nFecha: {self.fecha}\nDescripción: {self.descripcion}"    


# VETERINARIOS 
veterinario1 = Veterinario("Pablo Lopez", "Generalista")
veterinario2 = Veterinario("Luis Gonzalez", "Cirujano")


# MASCOTAS
mascota1 = Perro("Tobby", 5, 10, "Chow chow")
mascota2 = Gato("Pelusa", 2, 4.5, "amarillo")
mascota3 = Perro("Max", 4, 8, "Beagle")


#CLIENTES

cliente1 = Cliente("Juan Perez", "123-456-789")

cliente1.registrar_mascota(mascota1)
cliente1.registrar_mascota(mascota2)

mascotas_cliente1 = cliente1.ver_lista_de_mascotas()

for mascota in mascotas_cliente1:
    print(f"Mascota de {cliente1.nombre}: {mascota.nombre}")


# CITAS
cita1 = Cita("20-9-2023", "Consulta general", veterinario1, mascota1)
cita2 = Cita("25-10-2023", "Chequeo mensual", veterinario2, mascota2)
cita3 = Cita("05-12-2023", "Vacunación", veterinario1, mascota3)

veterinario1.registrar_cita(cita1)
veterinario2.registrar_cita(cita2)
veterinario1.registrar_cita(cita3)

print(cita1)  
print(veterinario1.lista_de_citas())
print(veterinario2.lista_de_citas())

#DIAGNOSTICOS

veterinario1.registrar_diagnostico(mascota1, "15-10-2023", "Lesion en la pata izquierda, aplicar cremas")
veterinario1.registrar_diagnostico(mascota3, "20-10-2023", "Anemia, seguir dieta especial por 1 mes")

diagnosticos_veterinario1 = veterinario1.mostrar_diagnostico()
for diagnostico in diagnosticos_veterinario1:
    print(diagnostico)