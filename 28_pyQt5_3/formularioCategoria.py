import sys
from PyQt5 import QtCore, QtWidgets, uic
 
qtCreatorFile = "frmCategoria.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class Formulario(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("frmCategoria.ui", self)

        self.btnProcesar.clicked.connect(self.procesar)
        self.btnBorrar.clicked.connect(self.borrar)
        self.btnSalir.clicked.connect(self.salir)

        self.show()
        
    def procesar(self):

        #entrada de datos
        nombre = self.txtNombre.text()
        promedio = int(self.txtPromedio.text())

        if promedio >= 17:
                categoria = "A"
        elif promedio >= 14:
                categoria = "B"
        elif promedio >= 12:
                categoria = "C"
        else:
                categoria = "D"

        
        self.txtResultado.setText(f"Nombre: {nombre} \nCategoría: {categoria} \n\nGracias por usar el programa!!" )



    def borrar(self):
        self.txtNombre.setText("")
        self.txtPromedio.setText("")
        self.txtResultado.setText("")
        
        
    def salir(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()