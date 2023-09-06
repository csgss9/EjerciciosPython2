class Gato:
    def sonido(self):
        return "miau"

class Perro:
    def sonido(self):
        return "guau"

gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido())