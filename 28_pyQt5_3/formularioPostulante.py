import sys
from PyQt5 import QtCore, QtWidgets, uic
 
qtCreatorFile = "frmPostulante.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class Formulario(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("frmPostulante.ui", self)

        self.btnAceptar.clicked.connect(self.aceptar)
        self.btnCerrar.clicked.connect(self.cerrar)
        

        self.rbMasculino.setChecked(True)


        self.show()
        
    def aceptar(self):
        
        #entrada
        nombre = self.txtNombre.text()     
        dni = int(self.txtDni.text())
        edad = int(self.spbEdad.value())
        modalidad = self.cboModalidad.currentText()
        area = self.cboArea.currentText()
        
        if modalidad == "Practicante":
                modalidad = "PR"
        if modalidad == "Medio Tiempo":
                modalidad = "MT"
        if modalidad == "Tiempo Completo":
                modalidad = "TC"
                
        if area == "Desarrollo de Sistemas":
                area = "DSI"
        if area == "Redes Informáticas":
                area = "RIN"
        if area == "Soporte Técnico":
                area = "STE"
        
        cat_edad = "" 
        if self.rbFemenino.isChecked() == True and edad < 23:
            cat_edad = "FA"
        elif self.rbFemenino.isChecked():
            cat_edad = "FB"
            
        elif self.rbMasculino.isChecked() == True and edad < 25:
            cat_edad = "MA"
        else:
            cat_edad = "MB"
        
        self.txtResultado.setText(f"Alumno: {nombre} \nCódigo: {modalidad}{area}{cat_edad}{dni}" )
       
        
        
    def cerrar(self):
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()