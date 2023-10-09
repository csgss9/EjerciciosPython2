from tkinter import *
from tkinter import messagebox

#creamos y configuramos la ventana

ventana = Tk()
ventana.title("Mi calculadora")
ventana.geometry("382x250")
ventana.configure(background = "yellow")

#Variable stringvar() para el resultado

resultado = StringVar()

#Funciones:

def suma():
    try:
        suma = int(txtPrimerNumero.get()) + int(txtSegundoNumero.get())
        return resultado.set(suma)
    except ValueError:
        messagebox.showinfo(title="ERROR", message="Ingresa un numero valido")
        txtPrimerNumero.delete(0, END)
        txtSegundoNumero.delete(0, END)
        resultado.set("")
        txtPrimerNumero.focus()   

def resta():
    try:
        resta = int(txtPrimerNumero.get()) - int(txtSegundoNumero.get())
        return resultado.set(resta)
    except ValueError:
        messagebox.showinfo(title="ERROR", message="Ingresa un numero valido")
        txtPrimerNumero.delete(0, END)
        txtSegundoNumero.delete(0, END)
        resultado.set("")
        txtPrimerNumero.focus()   
        
def multiplicacion():
    try:
        multiplicacion = int(txtPrimerNumero.get()) * int(txtSegundoNumero.get())
        return resultado.set(multiplicacion)
    except ValueError:
        messagebox.showinfo(title="ERROR", message="Ingresa un numero valido")
        txtPrimerNumero.delete(0, END)
        txtSegundoNumero.delete(0, END)
        resultado.set("")
        txtPrimerNumero.focus()   

def division():
    try:
        division = int(txtPrimerNumero.get()) / int(txtSegundoNumero.get())
        return resultado.set(division)
    except ZeroDivisionError:
        messagebox.showinfo(title = "ERROR", message = "No se puede dividir por 0")
        txtPrimerNumero.delete(0, END)
        txtSegundoNumero.delete(0, END)
        resultado.set("")
        txtPrimerNumero.focus()
    except ValueError:
        messagebox.showinfo(title="ERROR", message="Ingresa un numero valido")
        txtPrimerNumero.delete(0, END)
        txtSegundoNumero.delete(0, END)
        resultado.set("")
        txtPrimerNumero.focus()      
        
def cerrar():
    ventana.destroy()
        

#creamos las etiquetas

lblPrimerNumero = Label(ventana, text= "Primer numero", bg = "yellow", fg = "black", font = ("Tahoma", 15))
lblPrimerNumero.grid(row = 0, column = 0, padx = 5, pady = 5)

lblSegundoNumero = Label(ventana, text= "Segundo numero", bg = "yellow", fg = "black", font = ("Tahoma", 15))
lblSegundoNumero.grid(row = 1, column = 0, padx = 5, pady = 5)

#creamos las cajas de texto

txtPrimerNumero = Entry(ventana, width= 10, font = ("Tahoma", 15), justify= CENTER)
txtPrimerNumero.grid(row = 0, column= 1)

txtSegundoNumero = Entry(ventana, width= 10, font = ("Tahoma", 15), justify= CENTER)
txtSegundoNumero.grid(row = 1, column= 1)

#Botones
btnSuma = Button(ventana, text= "+", bg= "green", fg="white", font= ("Tahoma", 12), width=12, command= suma)
btnSuma.grid(row=2, column= 0, padx = 5, pady = 5)

btnMult = Button(ventana, text= "*", bg= "green", fg="white", font= ("Tahoma", 12), width=12, command= multiplicacion)
btnMult.grid(row=3, column= 0, padx = 5, pady = 5)

btnResta = Button(ventana, text= "-", bg= "green", fg="white", font= ("Tahoma", 12), width=12, command= resta)
btnResta.grid(row=2, column= 1, padx = 5, pady = 5)

btnDivision = Button(ventana, text= "/", bg= "green", fg="white", font= ("Tahoma", 12), width=12, command= division)
btnDivision.grid(row=3, column= 1, padx = 5, pady = 5)

btnCerrar = Button(ventana, text= "Cerrar", bg= "grey", fg="white", font= ("Tahoma", 12), width=30, command=cerrar)
btnCerrar.grid(row=4, column= 0, padx = 5, pady = 5, columnspan= 2)

#resultado

lblResultado = Label(ventana, bg= "white", width= 25, font = ("Tahoma", 15), textvariable= resultado)
lblResultado.grid(row = 5, column= 0, padx = 5, pady = 5, columnspan= 2)


ventana.mainloop()