from tkinter import *
from sqlite3 import *
from tkinter import messagebox
from random import *
import turtle

def FUNCIONP():

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    turtle.title("Muñeco Ahorcado")
    turtle.bgcolor("white")

    def dibujar_horca():
        t.penup()
        t.goto(-100, -100)
        t.pendown()
        t.forward(200)
        t.backward(100)
        t.left(90)
        t.forward(300)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(50)

    def dibujar_cabeza():
        t.penup()
        t.goto(100, 115)
        t.setheading(0)
        t.pendown()
        t.circle(20)

    def cuerpo():
        t.penup()
        t.goto(100,115)
        t.setheading(-90)
        t.pendown()
        t.forward(100)

    def manoizquierda():
        t.penup()
        t.goto(90,90)
        t.setheading(-135)
        t.pendown()
        t.forward(50)
    def manoderecha():
        t.penup()
        t.goto(110, 90)
        t.setheading(-35)
        t.pendown()
        t.forward(50)


    def piernas():
        t.penup()
        t.goto(90,10)
        t.setheading(-135)
        t.pendown()
        t.forward(50)

        t.penup()
        t.goto(110, 10)
        t.setheading(-35)
        t.pendown()
        t.forward(50)

    def dibujar_parte(fallos):
        if fallos == 1:
            dibujar_cabeza()
        elif fallos == 2:
            cuerpo()
        elif fallos == 3:
            piernas()

    base_de_datos = connect("palabras.db")
    cr = base_de_datos.cursor()


    def dibujar_parte(fallos):
        if fallos == 1:
            dibujar_cabeza()
        elif fallos == 2:
            cuerpo()
        elif fallos == 3:
            manoizquierda()
        elif fallos == 4:
            manoderecha()
        elif fallos == 5:
            piernas()

    base_de_datos = connect("palabras.db")
    cr = base_de_datos.cursor()

    app = Tk()
    app.title("AHORCADO")
    app.resizable(width=False, height=False)

    intentos = 3
    fallos = 0
    palabra = ""
    descripcion = ""

    caja = Entry(app)
    descripcion_label = Label(app, text="")
    btn_jugar = Button(app, text="Jugar", command=None)
    btn_reiniciar = Button(app, text="Jugar de nuevo", command=None)

    def nueva_partida():
        global intentos, fallos, palabra, descripcion



        cr.execute('''SELECT MAX(id) FROM palabras ''')
        resultado = cr.fetchone()[0]
        numero = randint(1,resultado)

        cr.execute('''SELECT palabra, descripcion FROM palabras WHERE id = ?''', (numero,))
        resultado = cr.fetchone()
        palabra = resultado[0]
        descripcion = resultado[1]

        intentos = 5
        fallos = 0

        cr.execute('''SELECT MAX(id) FROM palabras ''')
        resultados = cr.fetchone()[0]
        numero = randint(1,resultados)

        cr.execute('''SELECT palabra, descripcion FROM palabras WHERE id = ?''', (numero,))
        resultado = cr.fetchone()
        palabra = resultado[0]
        descripcion = resultado[1]

        while (palabra == "" and descripcion == ""):
            numero = randint(1,resultado)

        caja.delete(0, END)
        descripcion_label.config(text=descripcion)

        t.clear()
        dibujar_horca()

    def jugar():
        global intentos, fallos


        entrada = caja.get().strip()

        if entrada == "":
            messagebox.showwarning("Entrada vacía", "Por favor, escribe una palabra.")
            return
        elif entrada.lower() == palabra.lower():
            messagebox.showinfo("¡Ganaste!", f"Felicidades, la palabra era: {palabra}")
        else:
            intentos -= 1
            fallos += 1
            dibujar_parte(fallos)

            if intentos > 0:
                messagebox.showinfo("Incorrecto", f"Palabra incorrecta. Te quedan {intentos} intentos.")
                caja.delete(0, END)
            else:
                messagebox.showerror("¡Perdiste!", f"Se acabaron los intentos. La palabra era: {palabra}")
                caja.delete(0, END)

    Label(app, text="Ingresa la palabra:").grid(row=0, column=0, padx=5, pady=5)
    caja.grid(row=1, column=0, padx=5, pady=5)

    Label(app, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
    descripcion_label.grid(row=3, column=0, padx=5, pady=5)

    btn_jugar.config(command=jugar)
    btn_jugar.grid(row=4, column=0, padx=5, pady=5)

    btn_reiniciar.config(command=nueva_partida)
    btn_reiniciar.grid(row=5, column=0, padx=5, pady=10)


    nueva_partida()

    app.mainloop()

