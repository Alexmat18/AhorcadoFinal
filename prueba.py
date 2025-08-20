from sqlite3 import *
from tkinter import messagebox
#se hace la conexion con la base de datos
baseDeDatos=connect("palabras.db")
#se crea el cursor
cr=baseDeDatos.cursor()
#se crea la tabla
cr.execute('''
    CREATE TABLE IF NOT EXISTS palabras (
           id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
           palabra TEXT NOT NULL, 
           descripcion TEXT NOT NULL
    )''')

