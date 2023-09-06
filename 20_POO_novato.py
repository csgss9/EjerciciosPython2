class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def ladrar(self):
        print("guau guau")
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Raza: {self.raza}"

tobby = Perro("Tobby","labrador retriever")
max = Perro("Max", "Golden retriever")

print(tobby)
tobby.ladrar()
print(max)
max.ladrar()
