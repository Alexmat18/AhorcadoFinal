from tkinter import *
from sqlite3 import *
from tkinter import messagebox
from random import *



numero = randint(1, 7)

intentos = 3

        base_de_datos = connect("palabras.db")
        cr = base_de_datos.cursor()

        cr.execute('SELECT descripcion FROM palabras WHERE id = ?', (numero,))
        descripcion = cr.fetchall()[0][0]

        cr.execute('SELECT palabra FROM palabras WHERE id = ?', (numero,))
        palabra = cr.fetchall()[0][0]

        def jugar():
            global intentos

            entrada = caja.get()

            if entrada == "":
                messagebox.showwarning("Entrada vacía", "Por favor, escribe una palabra.")
                return
            elif entrada == palabra:
                messagebox.showinfo("¡Ganaste!", f"Felicidades, la palabra era: {palabra}")
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


        caja = Entry(app)
        caja.grid(row=0, column=0, padx=5, pady=5)


        Label(app, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        Label(app, text=descripcion).grid(row=2, column=0, padx=5, pady=5)


        btn = Button(app, text="Jugar", command=jugar)
        btn.grid(row=4, column=0, padx=5, pady=5)
        def jugar_de_nuevo():
            caja2 = Entry(app)
            caja2.grid(row=5, column=0, padx=5, pady=5)
            if caja2.get() == "":
                messagebox.showinfo("alerta","ingresa algo en la caja")
            elif caja2.get() == "si":



        messagebox.showinfo("si o no","quieres jugar de nuevo")
        btn = Button(app,text = "jugar de nuevo",command=jugar_de_nuevo)
        btn.grid(row=6, column=0, padx=5, pady=5)

        app.mainloop()



