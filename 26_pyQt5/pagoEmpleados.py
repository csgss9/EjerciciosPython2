import sys
from PyQt5 import QtCore, QtWidgets, uic
 
qtCreatorFile = "/home/computer/Documentos/EDDPOO_II.07.2023-IIIE/SEMANA5/frmPagoEmpleados.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class Formulario(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("/home/computer/Documentos/EDDPOO_II.07.2023-IIIE/SEMANA5/frmPagoEmpleados.ui", self)
       
        self.btnProcesar.clicked.connect(self.procesar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)

       
        self.show()
        
    def procesar(self):
        #entrada de datos
        horas = float(self.txtHoras.text())
        costoHoras = float(self.txtCosto.text())
        
        #proceso de calculo
        sueldoBasico = horas * costoHoras
        bonificacion = 0.20 * sueldoBasico
        sueldoBruto = sueldoBasico + bonificacion
        descuento = 0.12 * sueldoBruto
        sueldoNeto = sueldoBruto - descuento
        
        #salida de resultados
        self.lblMontoBruto.setText("$" + str("{:.2f}".format(sueldoBruto)))
        self.lblMontoNeto.setText("$" + str("{:.2f}".format(sueldoNeto)))
        self.lblMontoDescuento.setText("$" + str("{:.2f}".format(descuento)))

    def limpiar(self):
        self.txtEmpleado.setText("")
        self.txtHoras.setText("")
        self.txtCosto.setText("")

        self.lblMontoBruto.setText("")
        self.lblMontoDescuento.setText("")
        self.lblMontoNeto.setText("")
        
    def salir(self):
        self.close()

 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()