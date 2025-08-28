from tkinter import *
from sqlite3 import *
from tkinter import messagebox
from random import *

def datos():
        global intentos,numero,
# Elegir palabra aleatoria
numero = randint(1, 7)

# Intentos disponibles
intentos = 3

# Conexión con la base de datos
base_de_datos = connect("palabras.db")
cr = base_de_datos.cursor()

# Obtener descripción y palabra secreta
cr.execute('SELECT descripcion FROM palabras WHERE id = ?', (numero,))
descripcion = cr.fetchall()[0][0]

cr.execute('SELECT palabra FROM palabras WHERE id = ?', (numero,))
palabra = cr.fetchall()[0][0]

# Función para manejar el juego
def jugar():
    global intentos

    entrada = caja.get()

    if entrada == "":
        messagebox.showwarning("Entrada vacía", "Por favor, escribe una palabra.")
        return
    elif entrada == palabra:
        messagebox.showinfo("¡Ganaste!", f"Felicidades, la palabra era: {palabra}")
        finalizar_juego()
    else:
        intentos -= 1
        if intentos> 0:
            messagebox.showinfo("Incorrecto", f"Palabra incorrecta. Te quedan {intentos} intentos .")
            caja.delete(0, END)
        else:
            messagebox.showerror("¡Perdiste!", f"Se acabaron los intentos. La palabra era: {palabra}")
            caja.delete(0, END)



app = Tk()
app.title("AHORCADO")
app.resizable(width=False, height=False)

# Caja de texto
caja = Entry(app)
caja.grid(row=0, column=0, padx=5, pady=5)

# Etiqueta de descripción
Label(app, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
Label(app, text=descripcion).grid(row=2, column=0, padx=5, pady=5)

# Botón para jugar
btn = Button(app, text="Jugar", command=jugar)
btn.grid(row=4, column=0, padx=5, pady=5)

# Ejecutar la app
app.mainloop()
