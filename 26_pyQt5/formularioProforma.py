import sys
from PyQt5 import QtCore, QtWidgets, uic
 
qtCreatorFile = "frmProforma.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class Formulario(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("frmProforma.ui", self)

        self.btnCalcular.clicked.connect(self.calcular)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        
        self.rbInteres1.setChecked(True)
        self.rbMayorista.setChecked(True)


        self.show()
    
    def calcular(self):
        #entrada de datos
        precio = float(self.txtPrecio.text())
        cantidad = int(self.spbCantidad.value())
        
        #importe
        
        importe = precio * cantidad
        
        #porcentaje de descuento
        porcentajeDescuento = 0
        if self.rbMayorista.isChecked() == True:
            porcentajeDescuento = 4.5/100
        
        if self.rbMinorista.isChecked() == True:
            porcentajeDescuento = 1.9/100
        
        #descuento
        descuento = importe * porcentajeDescuento
        
        #porcentaje de interes
        
        porcentajeInteres = 0
        if self.rbInteres1.isChecked() == True:
            porcentajeInteres = 0/100
            
        if self.rbInteres2.isChecked() == True:
            porcentajeInteres = 8.5/100
        
        if self.rbInteres3.isChecked() == True:
            porcentajeInteres = 12.5/100
        
        #interes
        
        interes = importe * porcentajeInteres
        
        #total
        
        total = importe - descuento + interes
        
        #salida de resultados
        
        self.txtImporte.setText("s/. " + str(importe))
        self.txtDescuento.setText("s/. " + str(descuento))
        self.txtInteres.setText("s/. " + str(interes))
        self.txtTotal.setText("s/. " + str(total))
        
        # txtS.setPlainText("Este es un texto de ejemplo en QTextEdit.")
        
        # self.txtS.setText(""" 
        # ==================/n
        # |     PROFORMA    |
        # ==================
                          
        #                   """)
        resultados = f""" 
    ==================
    |     RESULTADOS     |
    ==================
    Monto Bruto: ${importe:.2f}
    Monto Descuento: ${descuento:.2f}
    Monto Neto: ${total:.2f}
    """

    # Mostrar la cadena en el QTextEdit
        self.txtS.setPlainText(resultados)

        
    def limpiar(self):
        pass
        # self.txtEmpleado.setText("")
        # self.txtHoras.setText("")
        # self.txtCosto.setText("")

        # self.lblMontoBruto.setText("")
        # self.lblMontoDescuento.setText("")
        # self.lblMontoNeto.setText("")
        
    def salir(self):
        self.close()

 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()