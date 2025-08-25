from tkinter import *
from sqlite3 import *
from tkinter import messagebox
from random import *

base_de_datos = connect("palabras.db")
cr = base_de_datos.cursor()



def juego():
    numero = randint(1, 9)

    palabra = cr.execute('''SELECT palabra FROM palabras where id = ?''',(numero,))

    descripcion=cr.execute('''SELECT descripcion FROM palabras where id = ?''',(numero,))

    etiqueta = Label(app,text = "Descripcion")
    etiqueta.grid(row = 1,column=0,padx = 5, pady = 5)

    texto = Label(app, text = f"{descripcion}")
    texto.grid(row = 2,column=0,padx = 5, pady = 5)

    i = 0
    while True:
        valor1 = caja.get()
        if palabra == valor1:
            messagebox.showinfo("felicidades ganaste",f"la palabra es: {palabra}")
            break
        elif i == 3:
            messagebox.showinfo("Lastima perdiste",f"la palabra es: {palabra}")
            break
        i = +1

app = Tk()
app.title("AHORCADO")
app.resizable(width=False,height=False)

caja = Entry(app)
caja.grid(row = 0, column = 0)

app.mainloop()