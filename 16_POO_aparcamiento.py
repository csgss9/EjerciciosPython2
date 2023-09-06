class Aparcamiento:
    
    def __init__(self, grandes, medianas, pequenas):
        self.grandes = grandes
        self.medianas = medianas
        self.pequenas = pequenas

    def aparcarCoche(self, tipoPlaza):
        if tipoPlaza == 1:
            if self.grandes > 0:
                self.grandes -= 1
                return True
            return False

        if tipoPlaza == 2:
            if self.medianas > 0:
                self.medianas -= 1
                return True
            return False

        if tipoPlaza == 3:
            if self.pequenas > 0:
                self.pequenas -= 1
                return True
            return False

aparcamiento = Aparcamiento(3, 2, 1)

for i in range(4):
    print(f'Vuelta {i}:')
    print(f' * aparcando coche grande: {aparcamiento.aparcarCoche(1)}')
    print(f' * aparcando coche mediano: {aparcamiento.aparcarCoche(2)}')
    print(f' * aparcando coche pequeño: {aparcamiento.aparcarCoche(3)}')

