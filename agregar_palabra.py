from sqlite3 import * 
from tkinter import messagebox
from tkinter import *
from tkinter import ttk #libreria para trabajar con tablas

#----------------------------------------------
#funcion para ver las palabras de la base de datos
def verPalabras():
    # Crear ventana emergente
    ventanaTabla = Toplevel(app)
    ventanaTabla.title("Palabras registradas")
    ventanaTabla.geometry("600x300")

    # Crear tabla Treeview
    tabla = ttk.Treeview(ventanaTabla, columns=("ID","Palabra", "Descripcion"), show="headings")
    tabla.heading("ID", text="ID")
    tabla.heading("Palabra", text="Palabra")
    tabla.heading("Descripcion", text="Descripción")
    tabla.pack(fill="both", expand=True)

    # Scroll vertical
    scroll = ttk.Scrollbar(ventanaTabla, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")

    # Llenar la tabla con datos
    cr.execute('SELECT * FROM palabras')
    palabras = cr.fetchall()
    for palabra in palabras:
        tabla.insert("", "end", values=palabra)
#---------------------------------------------
# funcion para agregar la palabra
def agregarPalabra():
    #se almacena el valor de las varibles en las cajas
    nuevaPalabra = str(nombrePalabra.get())
    nuevaDescripcion = descripcion.get("1.0", "end")
    #se reconfigura la etiqueta de cada caja
    resultad2.configure(text=f"La palabra es {nuevaPalabra}")
    resultado.configure(text=f"Descripcion: {nuevaDescripcion}")
    cr.execute('''
        INSERT INTO palabras (palabra, descripcion)
        VALUES (?,?)''', (nuevaPalabra, nuevaDescripcion))
    baseDeDatos.commit()


#---------------------------------
baseDeDatos=connect("palabras.db")
#se crea el cursor
cr=baseDeDatos.cursor()
#se crea la ventana principal 
app=Tk()
#se crea el titulo
app.title("Agregar Palabra")

#se crea el tamaño de la ventana
#app.geometry("500x400")
#app.resizable(False,False)
#---------------------------------------------------
#
#----------------------------------------------
#etiqueta para dar la bienvenida
etiqueta1=Label(app, text="Agregue una palabra nueva", font=(25))
etiqueta1.grid(row=0, column=0, sticky="wens", columnspan=4)
#etiqueta y entry para la palbra
etiqueta2=Label(app, text='Ingrese la palabra: ', fg='blue', font=(20))
etiqueta2.grid(row=1, column=0, sticky='wens', columnspan=2)
nombrePalabra=Entry(app)
nombrePalabra.grid(row=1, column=2, sticky='wens', columnspan=4)
#etiqueta para la descripcion
etiqueta3=Label(app, text='Ingrese la descripcion: ', fg='blue', font=(20))
etiqueta3.grid(row=2, column=0, sticky='wens', columnspan=2)
descripcion=Text(app, height=5, width=30)
descripcion.grid(row=2, column=2, sticky='wens', columnspan=3, pady=5, padx=3)
#------------------------------------------------
#varibles para almacenar las palabras y la descripcion
resultado=Label(app, text="La palabra es: ")
resultad2=Label(app, text="La descripcion es: ")

resultado.grid(row=3, column=0, columnspan=3)
resultad2.grid(row=4, column=0, columnspan=3)
#------------------------------------------------------
#boton de agregar
resul=Button(app, text="Agregar", command=agregarPalabra)
resul.grid(row=5, column=0)
#boton para ver las palabras
ver=Button(app, text="Ver Palabras", command=verPalabras)
ver.grid(row=5, column=1)

app.mainloop()