from tkinter import *
from sqlite3 import *
from tkinter import messagebox
from random import *

numero = randint(1, 7)

def jugar():
        if valor1 == palabra:
            messagebox.showinfo("felicidades ganaste", f"la palabra es: {palabra}")

        else:
            messagebox.showinfo("Lastima perdiste", f"la palabra es: {palabra}")

base_de_datos = connect("palabras.db")
cr = base_de_datos.cursor()

app = Tk()
app.title("AHORCADO")
app.resizable(width=False,height=False)

caja = Entry(app)
caja.grid(row = 0, column = 0, padx=5, pady=5)

cr.execute('''SELECT descripcion FROM palabras WHERE id = ? ''', (numero,))
descripcion =  cr.fetchall()

etiqueta = Label(app, text="Descripcion")
etiqueta.grid(row=1, column=0, padx=5, pady=5)

texto = Label(app, text=f"{descripcion}")
texto.grid(row=2, column=0, padx=5, pady=5)


cr.execute('''SELECT palabra FROM palabras WHERE id = ?''', (numero,))
palabra = cr.fetchall()

valor1 = caja.get()

for i in range(0, 3):
    jugar()

app.mainloop()