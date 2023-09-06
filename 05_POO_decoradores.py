class Persona:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @name.deleter
    def name(self):
        del self.__name

objeto = Persona("Martin")

name = objeto.name
print(name)

objeto.name = "Sofia"
print(objeto.name)

del objeto.name
print(objeto.name)