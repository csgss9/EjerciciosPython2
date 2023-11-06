import sys
from PyQt5 import QtCore, QtWidgets, uic
 
qtCreatorFile = "frmRegistroVentas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

lista = []


class Formulario(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("frmRegistroVentas.ui", self)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnNuevo.clicked.connect(self.nuevo)
        self.btnSalir.clicked.connect(self.salir)
        
        self.show()
    
    def registrar(self):
        
        #entrada de datos
        
        dia = self.dtFecha.date().day()
        mes = self.dtFecha.date().month()
        año = self.dtFecha.date().year()
        fecha = str(dia) + "/" + str(mes) + "/" + str(año)
        
        
        producto = self.cboProducto.currentText()
        tipoPago = self.cboPago.currentText()
        cantidad = int(self.txtCantidad.text())
        
        #precio del producto
        precio = 0
        if producto == "Colección Escolar":
            precio = 240 
        
        if producto == "Colección PreUniversitaria":
            precio = 150
            
        if producto == "Colección Profesional":
            precio = 350

        self.lblPrecio.setText("s/. " + str(precio))
        
        #calculamos subtotal
        subTotal = precio * cantidad
        
        #calculamos descuento y recargo
        
        descuento = 0
        recargo = 0
        
        if tipoPago == "Contado":
            descuento = 0.05 * subTotal
        if tipoPago == "Tarjeta":
            recargo = 0.10 * subTotal
            
        #precio final
        precioFinal = subTotal - descuento + recargo
        
        #datos en la lista y mostrarlos en la tabla
        datos = (producto, str(cantidad), "s/. " + str(precio), tipoPago, "s/. " + str(descuento), "s/." + str(recargo), "s/. " + str(precioFinal), fecha)
        lista.append(datos)
        
        self.listar()
        # self.limpiarControles()
        
    def listar(self):
        self.tblDatos.setRowCount(50)
        for i in range(len(lista)):
            self.tblDatos.setItem(i, 0, QtWidgets.QTableWidgetItem(lista[i][0]))
            self.tblDatos.setItem(i, 1, QtWidgets.QTableWidgetItem(lista[i][1]))
            self.tblDatos.setItem(i, 2, QtWidgets.QTableWidgetItem(lista[i][2]))
            self.tblDatos.setItem(i, 3, QtWidgets.QTableWidgetItem(lista[i][3]))
            self.tblDatos.setItem(i, 4, QtWidgets.QTableWidgetItem(lista[i][4]))
            self.tblDatos.setItem(i, 5, QtWidgets.QTableWidgetItem(lista[i][5]))
            self.tblDatos.setItem(i, 6, QtWidgets.QTableWidgetItem(lista[i][6]))
            self.tblDatos.setItem(i, 7, QtWidgets.QTableWidgetItem(lista[i][7]))

    def limpiarControles(self):
        self.txtCantidad.clear()
        self.lblPrecio.clear()
        self.cboProducto.setCurrentIndex(0)
        self.cboPago.setCurrentIndex(0)                
            
    
    def limpiarTabla(self):
        self.tblDatos.clearContents()
        self.tblDatos.setRowCount(0)
    
    def nuevo(self):
        self.limpiarControles()
        self.limpiarTabla()

    def salir(self):
        self.close()

 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()