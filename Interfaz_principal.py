from customtkinter import *
from tkinter import *
from agregar_palabra import *
from agregar_palabra import principal
from juego import *

#funcion para cerrar la ventana principal
def salir():
    app.destroy()

app=CTk()
app.title("INTERFAZ PRINCIPAL")
fuente=CTkFont(family="Arial", size=30, weight="bold")
fuente2=CTkFont(family="Arial", size=25, weight="bold")

#creacion de  los marcos
marco3=CTkFrame(app,bg_color='lightYellow', width=100, height=100)
marco1=CTkFrame(app,bg_color='lightYellow', width=100, height=100)
marco2=CTkFrame(app,bg_color='white', width=100, height=10)
marco1.grid(row=0, column=0, columnspan=3, sticky="news")
marco2.grid(row=1, column=0, columnspan=3)
marco3.grid(row=2, column=0, columnspan=3,sticky="news")
#texto de bievenida
etiquetaBienve=CTkLabel(marco1, text="Bienvenido al menú principal", font=fuente)
etiquetaBienve1=CTkLabel(marco1, text="Presione un boton para elegir lo que quiere hacer",font=fuente2)
etiquetaBienve.grid(row=0, column=0, columnspan=3)
etiquetaBienve1.grid(row=1, column=0, columnspan=3)
#-----------------------------------------------------
#etiqueta par el marco 3
etiqueta4=CTkLabel(marco3, text="Jugar es la forma más divertida que tiene nuestro cerebro de aprender", font=fuente2)
etiqueta4.grid(row=0, column=0, columnspan=1, rowspan=3)
#creacion de los botones para realizar acciones
botonJugar=CTkButton(marco2, text="Jugar", command=FUNCIONP)

botonAcciones=CTkButton(marco2, text="Acciones", command=principal)
botonSalir=CTkButton(marco2, text="Salir", command=salir)
#invocar los botones
botonSalir.grid(row=0, column=0, pady=5, padx=5)
botonJugar.grid(row=0, column=1, pady=5, padx=5)
botonAcciones.grid(row=0, column=2, pady=5, padx=5)
app.mainloop()