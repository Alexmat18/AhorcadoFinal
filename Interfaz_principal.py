from tkinter import *
#funcion para cerrar la ventana principal
def salir():
    app.destroy()

app=Tk()
app.title("INTERFAZ PRINCIPAL")

#creacion de  los marcos
marco1=Frame(app,bg='lightYellow', width=100, height=100)
marco2=Frame(app,bg='lightpink', width=100, height=10)
marco1.grid(row=0, column=0, columnspan=3)
marco1.grid(row=1, column=0, columnspan=3)
#creacion de los botones para realizar acciones
botonJugar=Button(marco1, text="Jugar")
botonAcciones=Button(marco1, text="Acciones")
botonSalir=Button(marco1, text="Salir", command=salir)
#invocar los botones
botonSalir.grid(row=0, column=0, pady=5, padx=5)
botonJugar.grid(row=0, column=1, pady=5, padx=5)
botonAcciones.grid(row=0, column=2, pady=5, padx=5)
app.mainloop()