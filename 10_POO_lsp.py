"""
Principios SOLID:

isp - principio de segregacion de interfaz:
    Una clase no debe depender de interfaces que no utiliza. Se debe definir interfaces
específicas para cada clase que se puedan heredar en lugar de tener interfaces generales que contengan métodos innecesarios para otras de sus subclases .

dip - principio de inversion de dependencias
    No depender de detalles. Los módulos de alto nivel no deben depender de módulos de bajo nivel, sino que ambos deben depender de abstracciones
Asi las clases de alto nivel se mantengan independientes de las de bajo nivel.

"""

from abc import ABC, abstractmethod

#procesamiento básico de documentos
class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def read(self):
        pass

#documentos PDF
class PDFDocument(ABC):
    @abstractmethod
    def extract_text(self):
        pass

# txt
class TextDocument(Document):
    def open(self):
        print("Abriendo documento de texto")

    def read(self):
        print("Leyendo documento de texto")

# Implementación de documento PDF
class PDFDocument(Document, PDFDocument):
    def open(self):
        print("Abriendo documento PDF")

    def read(self):
        print("Leyendo documento PDF")

    def extract_text(self):
        print("Extrayendo texto de documento PDF")