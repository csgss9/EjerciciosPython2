""" Herencia mutiple"""

class Animal:
    pass
    def comer(self):
        print("El animal está comiendo")

class Mamifero(Animal):
    pass
    
    def amamantar(self):
        print("El animal está amamantando")

class Ave(Animal):
    pass

    def volar(self):
        print("El animal está volando")

class Murcielago(Mamifero,Ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()

ave = Ave()

ave.comer()
ave.volar()

print(Murcielago.mro())