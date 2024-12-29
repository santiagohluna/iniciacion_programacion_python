import mysql.connector
import sqlite3

def crear_tabla_inventario():
    conexion = sqlite3.connect("PFI_Python.db")
    cursor = conexion.cursor()
    # cursor.execute("DROP TABLE IF EXISTS inventario")
    conexion.commit()
    cursor.execute(
    '''CREATE TABLE "inventario" (
	"Código" INTEGER,
	"Nombre" varchar(50) NOT NULL,
	"Descripción" varchar(200),
	"Cantidad" int NOT NULL,
	"Precio" double NOT NULL,
	"Categoría" varchar(50),
	PRIMARY KEY("Código" AUTOINCREMENT)
    );'''
    )
    conexion.commit()
    conexion.close()

# def crear_tabla_inventario():
#     mibd = mysql.connector.connect(
#         host = 'localhost',
#         user = 'root'
#     )

#     # Se crea una instancia de la clase 'cursor' el cual se usa para ejecutar comandos SQL.
#     cursor = mibd.cursor()

#     # Se ejecuta un comando SQL.
#     cursor.execute("USE PFI_Python;")

#     cursor.execute(
#         '''CREATE TABLE IF NOT EXISTS inventario(
#             ID_Articulo int primary key,
#             Nombre varchar(50) not null,
#             Descripcion varchar(200),
#             Cantidad int not null,
#             Precio double not null,
#             Categoria varchar(50)
#         );'''
#     )
    
#     cursor.close()

crear_tabla_inventario()