from tkinter import *
from sqlite3 import *
from tkinter import messagebox
from random import *

numero = randint(1, 7)
i = 3
estado = True
def jugar():

        valor1 = caja.get()
        print(valor1)
        if valor1 == dato:
                messagebox.showinfo("felicidades ganaste", f"la palabra es: {dato}")
        else:
                estado = False
        if estado == False:
                messagebox.showinfo("ops", f"te quedan {i-1} intentos")
                valor1 = caja.get()
                caja.delete(0,END)

print(estado)
print(i)
base_de_datos = connect("palabras.db")
cr = base_de_datos.cursor()

app = Tk()
app.title("AHORCADO")
app.resizable(width=False,height=False)

caja = Entry(app)
caja.grid(row=0, column=0, padx=5, pady=5)

cr.execute('''SELECT descripcion FROM palabras WHERE id = ? ''', (numero,))
descripcion =  cr.fetchall()

etiqueta = Label(app, text="Descripcion")
etiqueta.grid(row=1, column=0, padx=5, pady=5)

texto = Label(app, text=f"{descripcion}")
texto.grid(row=2, column=0, padx=5, pady=5)


cr.execute('''SELECT palabra FROM palabras WHERE id = ?''', (numero,))
palabra = cr.fetchall()
dato = palabra[0][0]
print(dato)

btn = Button(app, text="Jugar", command=jugar)
btn.grid(row=4, column=0, padx=5, pady=5)




app.mainloop()