from sqlite3 import * 
from tkinter import messagebox
from tkinter import *
from tkinter import ttk #libreria para trabajar con tablas



#funcion principla
def principal():
    # ----------------------------------------------
    # funcion para cerrar la ventana principal
    def cerrarVentanaPrincipal():
        app.destroy()

    # funcion para ver las palabras de la base de datos
    def verPalabras():
        # funcion para hacer que la ventana se cierrre
        def cerrarVentana():
            ventanaTabla.destroy()

        # Crear ventana emergente
        ventanaTabla = Toplevel(app)
        ventanaTabla.title("Palabras registradas")
        # ventanaTabla.geometry("600x300")

        # Crear tabla Treeview
        tabla = ttk.Treeview(ventanaTabla, columns=("ID", "Palabra", "Descripcion"), show="headings")
        tabla.column("ID", width=20, anchor="center")
        tabla.heading("ID", text="ID")
        tabla.heading("Palabra", text="Palabra")
        tabla.heading("Descripcion", text="Descripción")

        tabla.grid(row=0, column=0, columnspan=3)
        # boton para cerrar la ventana
        botonCerrar = Button(ventanaTabla, text="Cerrar", command=cerrarVentana)
        botonCerrar.grid(row=1, column=0, padx=10, pady=10)

        # Llenar la tabla con datos
        cr.execute('SELECT * FROM palabras')
        palabras = cr.fetchall()
        for palabra in palabras:
            tabla.insert("", "end", values=palabra)

    # -----------------------------------------------------------------------------------------------------------------
    # funcion para eliminar las palabras en base al ID, se crea una ventana emergente para mejor estetica
    def eliminarPalabras():  # funcion para realizar la funcion de eliminar palabras
        def eliminar():  # funcion para eliminar la palabra
            # validacion de los campos
            if IdEliminado.get() == "":
                messagebox.showwarning("Advertencia", "Por favor, ingrese un ID.")
            else:
                id_palabra = IdEliminado.get()  # se guarda el numero ingresado por el usuario
                cr.execute('DELETE FROM palabras WHERE id = ?', (id_palabra,))  # se elimina la palabra en base al ID
                baseDeDatos.commit()  # GUARDA LOS Cambios en la base de datos
                messagebox.showinfo("Accion exitosa",
                                    f"La palabra con ID {id_palabra} fue eliminada con exito")  # muestra un mensaje una vez se eliminó la palabra
                ventanaEliminar.destroy()  # Se destruye la ventana emergente una vez se elimina la palabra

        # Crear ventana emergente
        ventanaEliminar = Toplevel(app)
        ventanaEliminar.title("Eliminar Palabra")
        # ventanaEliminar.geometry("300x150")

        # Etiqueta y campo de entrada para el ID
        etiqueta1 = Label(ventanaEliminar, text="Ingrese el ID de la palabra a eliminar:")
        etiqueta1.grid(row=0, column=0, pady=10)
        IdEliminado = Entry(ventanaEliminar)
        IdEliminado.grid(row=1, column=0, pady=5)

        # Botón para eliminar la palabra en la ventana emergente para eliminar la palabra
        botonEliminar = Button(ventanaEliminar, text="Eliminar", command=eliminar)
        botonEliminar.grid(row=2, column=0, pady=10)

    # ---------------------------------------------
    # funcion para agregar la palabra
    def agregarPalabra():
        # validacion de los campos
        if nombrePalabra.get() == "" or descripcion.get() == "\n":
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

            return
        else:
            # se almacena el valor de las varibles en las cajas
            nuevaPalabra = str(nombrePalabra.get())
            nuevaDescripcion = descripcion.get()
            # se reconfigura la etiqueta de cada caja
            resultad2.configure(text=f"La palabra es {nuevaPalabra}")
            resultado.configure(text=f"Descripcion: {nuevaDescripcion}")
            cr.execute('''
                INSERT INTO palabras (palabra, descripcion)
                VALUES (?,?)''', (nuevaPalabra, nuevaDescripcion))
            baseDeDatos.commit()
            messagebox.showinfo("Accion exitosa", "La palabra fue agregada con exito")
            nombrePalabra.delete(0, END)
            descripcion.delete(0, END)

    # ---------------------------------
    #---------------------------------------------
    baseDeDatos = connect("palabras.db")
    # se crea el cursor
    cr = baseDeDatos.cursor()
    # se crea la ventana principal
    app = Tk()
    # se crea el titulo
    app.title("Agregar Palabra")
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
    descripcion=Entry(app, width=30)
    descripcion.grid(row=2, column=2, sticky='wens', columnspan=3, pady=5, padx=3)
    #E
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
    #Boton para abrir la ventana de eliminar una palabra
    eliminar=Button(app, text="Eliminar palabra", command=eliminarPalabras)
    eliminar.grid(row=5, column=2)
    #Boton para cerrar la ventana principal
    cerrarP=Button(app, text='Cerrar', command=cerrarVentanaPrincipal)
    cerrarP.grid(row=5, column=3)
    app.mainloop()


