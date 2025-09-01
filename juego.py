from tkinter import *
from sqlite3 import *
from tkinter import messagebox
from random import *


# Conectar a la base de datos
base_de_datos = connect("palabras.db")
cr = base_de_datos.cursor()


# Crear ventana principal
app = Tk()
app.title("AHORCADO")
app.resizable(width=False, height=False)

# Variables globales
intentos = 3
palabra = ""
descripcion = ""

# Widgets (se actualizan después)
caja = Entry(app)
descripcion_label = Label(app, text="")
btn_jugar = Button(app, text="Jugar", command=None)
btn_reiniciar = Button(app, text="Jugar de nuevo", command=None)


def nueva_partida():
    global intentos, palabra, descripcion

    # Restablecer intentos
    intentos = 3

    # Elegir nueva palabra
    numero = randint(1, 7)
    cr.execute('SELECT descripcion FROM palabras WHERE id = ?', (numero,))
    descripcion = cr.fetchone()[0]

    cr.execute('SELECT palabra FROM palabras WHERE id = ?', (numero,))
    palabra = cr.fetchone()[0]

    # Actualizar UI
    caja.delete(0, END)
    descripcion_label.config(text=descripcion)


def jugar():
    global intentos

    entrada = caja.get().strip()

    if entrada == "":
        messagebox.showwarning("Entrada vacía", "Por favor, escribe una palabra.")
        return
    elif entrada.lower() == palabra.lower():
        messagebox.showinfo("¡Ganaste!", f"Felicidades, la palabra era: {palabra}")
    else:
        intentos -= 1
        if intentos > 0:
            messagebox.showinfo("Incorrecto", f"Palabra incorrecta. Te quedan {intentos} intentos.")
            caja.delete(0, END)
        else:
            messagebox.showerror("¡Perdiste!", f"Se acabaron los intentos. La palabra era: {palabra}")
            caja.delete(0, END)


# Posicionar widgets
Label(app, text="Ingresa la palabra:").grid(row=0, column=0, padx=5, pady=5)
caja.grid(row=1, column=0, padx=5, pady=5)

Label(app, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
descripcion_label.grid(row=3, column=0, padx=5, pady=5)

btn_jugar.config(command=jugar)
btn_jugar.grid(row=4, column=0, padx=5, pady=5)

btn_reiniciar.config(command=nueva_partida)
btn_reiniciar.grid(row=5, column=0, padx=5, pady=10)

# Iniciar primera partida
nueva_partida()

# Ejecutar aplicación
app.mainloop()

