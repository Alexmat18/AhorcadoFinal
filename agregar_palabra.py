from sqlite3 import * 
from tkinter import messagebox
from tkinter import *

#----------------------------------------------
#lista para almacenar la palabra
listaDePlabras=[]
#lista para almacenar las descripciones
descripciones=[]
#---------------------------------------------

baseDeDatos=connect("palabras.db")
#se crea el cursor
cr=baseDeDatos.cursor()
#se crea la ventana principal 
app=Tk()
#se crea el titulo
app.title("Agregar Palabra")

#se crea el tamaño de la ventana
app.geometry("400x300")
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
descripcio=Text(app, height=5, width=30)
descripcio.grid(row=2, column=2, sticky='wens', columnspan=4)
#------------------------------------------------
#funcion para agregar las palabras

app.mainloop()