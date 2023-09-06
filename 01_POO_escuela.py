""" Herencia Simple"""

class Persona:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Nombre: {self.name} \n Edad: {self.age}'

name = input("Ingrese nombre de la persona: ")
age = int(input("Ingrese edad de la persona: "))
grade = input("Ingrese grado del estudiante: ")

class Estudiante(Persona):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade

    def __str__(self):
        return f'Nombre: {self.name} \n Edad: {self.age} \n Grado: {self.grade}'

estudiante1 = Estudiante(name, age, grade)

print(estudiante1)

    



