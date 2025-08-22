from sqlite3 import * 
from tkinter import messagebox, Button
from tkinter import *

#----------------------------------------------
#lista para almacenar la palabra
listaDePlabras=[]
#lista para almacenar las descripciones
descripciones=[]
#---------------------------------------------
# funcion para agregar la palabra
def agregarPalabra():
    nuevaPalabra = str(nombrePalabra.get())
    nuevaDescripcion = descripcion.get("1.0", "end")
    resultad2.configure(text=f"El valor es {nuevaDescripcion}")
    resultado.configure(text=f"El valor es {nuevaPalabra}")

#---------------------------------
baseDeDatos=connect("palabras.db")
#se crea el cursor
cr=baseDeDatos.cursor()
#se crea la ventana principal 
app=Tk()
#se crea el titulo
app.title("Agregar Palabra")

#se crea el tamaño de la ventana
app.geometry("400x400")
app.resizable(False,False)
#----------------------------------------------
#etiqueta para dar la bienvenida
etiqueta1=Label(app, text="Agregue una palabra nueva", bg="lightgreen", fg="blue", font=(25))
etiqueta1.grid(row=0, column=0, sticky="wens", columnspan=4)
#etiqueta y entry para la palbra
etiqueta2=Label(app, text='Ingrese la palabra: ', bg='lightgreen', fg='blue', font=(20))
etiqueta2.grid(row=1, column=0, sticky='wens', columnspan=2)
nombrePalabra=Entry(app)
nombrePalabra.grid(row=1, column=2, sticky='wens', columnspan=4)
#etiqueta para la descripcion
etiqueta3=Label(app, text='Ingrese la descripcion: ', bg='lightgreen', fg='blue', font=(20))
etiqueta3.grid(row=2, column=0, sticky='wens', columnspan=2)
descripcion=Text(app, height=5, width=30)
descripcion.grid(row=2, column=2, sticky='wens', columnspan=3, pady=5, padx=3)
#------------------------------------------------
#varibles para almacenar las palabras y la descripcion


resultado=Label(app, text="El valor es: ")

resultad2=Label(app, text="El valor es: ")

resultado.grid(row=3, column=0)
resultad2.grid(row=4, column=0, columnspan=3)

#------------------------------------------------------
#boton de agregar
resul=Button(app, text="Agregar", command=agregarPalabra)
resul.grid(row=5, column=0)


app.mainloop()