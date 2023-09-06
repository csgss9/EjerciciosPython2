class Persona:
    def __init__(self, name):
        self.__name = name

    def get__name(self):
        return self.__name

    def set__name(self, new_name):
        self.__name = new_name

objeto = Persona("Martin")

name = objeto.get__name()
print(name)
objeto.set__name("Sofia")

name = objeto.get__name()
print(name)