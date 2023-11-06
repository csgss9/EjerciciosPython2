import sys
from PyQt5 import QtCore, QtWidgets, uic
 
qtCreatorFile = "frmPagos.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

lista = []
 
class Formulario(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("frmPagos.ui", self)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnSalir.clicked.connect(self.salir)

        self.show()
        
    def registrar(self):
        
       #entrada de datos
        empleado = self.txtEmpleado.text()

        categoria = self.cboCategoria.currentText()
        
        #sueldo
        
        sueldo = 0
        if categoria == "JEFE":
            sueldo = 3500
        
        if categoria == "ADMINISTRATIVO":
            sueldo = 2500
            
        if categoria == "TECNICO":
            sueldo = 1700
        
        if categoria == "OPERACION":
            sueldo = 1000 

        self.lblSueldo.setText("s/. " + str(sueldo))
        
        #descuento
        if sueldo > 2000:
            descuento = sueldo * 0.125
        else:
            descuento = 0
        
        neto = sueldo - descuento
        
        datos = (empleado, categoria, "s/. " + str(sueldo), "s/. " + str(descuento), "s/." + str(neto))
        lista.append(datos)
        
        self.listar()    

    def listar(self):
        self.tblPagos.setRowCount(50)
        for i in range(len(lista)):
            self.tblPagos.setItem(i, 0, QtWidgets.QTableWidgetItem(lista[i][0]))
            self.tblPagos.setItem(i, 1, QtWidgets.QTableWidgetItem(lista[i][1]))
            self.tblPagos.setItem(i, 2, QtWidgets.QTableWidgetItem(lista[i][2]))
            self.tblPagos.setItem(i, 3, QtWidgets.QTableWidgetItem(lista[i][3]))
            self.tblPagos.setItem(i, 4, QtWidgets.QTableWidgetItem(lista[i][4]))

    def cancelar(self):
        self.tblPagos.clearContents()
        self.tblPagos.setRowCount(0)        
    
    def salir(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()