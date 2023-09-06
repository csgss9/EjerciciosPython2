"""
Principios SOLID:

ocp - principio de abierto/cerrado:
    Las clases, metodos... deben estar abiertas para la extension pero cerradas para la 
modificación. Es decir se deberia poder agregar nuevas funcionalidades sin modificar el
codigo fuente

lsp - principio de sustitucion de liskov:
    Si la clase B es una subclase de A. A deberia poder usarse en cualquier lado que
se use B.

En la clase se padre se define lo que todas las subclases tienen en comun. Para que 
todas las subclases puedan hacer lo que la clase padre puede.


"""

class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

#Para no modificar esta clase agregando nuevas funciones

    def notificar(self):
        raise NotImplementedError  #Obliga al dev a crear la clase notificar

#Creamos clases nuevas con las funcionalidades a añadir:

class NotificadorSMS(Notificador):
    def notificar(self):
        print("Enviando por SMS")

class NotificadorWhatsapp(Notificador):
    def notificar(self):
        print("Enviando por Whatsapp")