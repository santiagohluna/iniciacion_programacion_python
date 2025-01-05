import os
import sqlite3
import numpy as np
import pandas as pd

# Crear la conexión a la base de datos.
conexion = sqlite3.connect("PFI_Python.db")
cursor = conexion.cursor()

opciones_menu_ppal = {
        1: "Alta de productos nuevos",
        2: "Consultar datos de productos",
        3: "Modificar la información de un producto",
        4: "Eliminar productos",
        5: "Salir",
    }


opciones_modificar = {1: "Modificar el nombre del producto",
            2: "Modificar la descripción del producto",
            3: "Modificar la cantidad en stock",
            4: "Modificar el precio del producto",
            5: "Modificar la categoría del producto"
            }

campos = ["Código",
         "Nombre",
         "Descripción",
         "Cantidad",
         "Precio",
         "Categoría"]

# Limpiar pantalla
def limpiar_pantalla():
    os.system("clear")

# Función para agregar productos.
def agregar_producto():

    titulo_registro = "Alta de productos"

    continuar = (
                input("¿Desea agregar un producto? Ingrese 's' o '[n]': ").lower() == "s"
            )
    print(" ")
    while continuar:

        limpiar_pantalla()
        print(" ")
        print("=" * len(titulo_registro))
        print(titulo_registro)
        print("=" * len(titulo_registro))
        print(" ")

        # Ingresar los datos del producto a agregar.
        try:
            codigo = int(input("Ingrese el código del producto: "))
        except:
            print("\nDebe ingresar un número.\n")
            continuar = True
        else:
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese una descripción del producto: ")
            cont = True
            while cont:
                try:
                    cantidad = int(input("Ingrese la cantidad en stock: "))
                except:
                    print("\nDebe ingresar un número natural.\n")
                    cont = True
                else:
                    cont = False
            cont = True
            while cont:
                try:
                    precio = float(input("Ingrese el precio del producto: "))
                except:
                    print("\nDebe ingresar un número real.\n")
                else:
                    cont = False
            
            categoria = input("Ingrese la categoría del producto: ")

            # Agregar el producto a la base de datos.
            cursor.execute("INSERT INTO inventario(Código, Nombre, Descripción, Cantidad, Precio, Categoría) VALUES (?, ?, ?, ?, ?, ?)",(codigo,nombre,descripcion,cantidad,precio,categoria))

            # Confirmar cambios.
            conexion.commit()

            # Producto registrado con éxito.
            print(f"\nProducto registrado con el código {codigo}.\n")

            continuar = (
                input("¿Desea agregar otro producto? Ingrese 's' o '[n]': ").lower() == "s"
            )
            print(" ")

def imprimir_resultados(resultados):

    titulo_codigo = "Código"
    titulo_nombre = "Nombre del producto"
    titulo_descripcion = "Descripción"
    titulo_precio = "Precio"
    titulo_cantidad = "Cantidad en stock"
    titulo_categoria = "Categoría"

    n_caracteres = [0,0,0,0,0,0]

    if resultados:

        n_codigos = []
        n_nombres = []
        n_descripciones = []
        n_cantidades = []
        n_precios = []
        n_categorias = []

        for registro in resultados:
                n_codigo = len(str(registro[0]))
                n_nombre = len(registro[1])
                n_descripcion = len(registro[2])
                n_cantidad = len(str(registro[3]))
                n_precio = len(str(registro[4]))
                n_categoria = len(registro[5])

                n_codigos.append(n_codigo)
                n_nombres.append(n_nombre)
                n_descripciones.append(n_descripcion)
                n_cantidades.append(n_cantidad)
                n_precios.append(n_precio)
                n_categorias.append(n_categoria)

        nmax_codigos = np.max(n_codigos)
        nmax_nombres = np.max(n_nombres)
        nmax_descripciones = np.max(n_descripciones)
        nmax_cantidades = np.max(n_cantidades)
        nmax_precios = np.max(n_precios)
        nmax_categorias = np.max(n_categorias)

        if (len(titulo_codigo) <= nmax_codigos):
            n_caracteres[0] = nmax_codigos
        else:
            n_caracteres[0] = len(titulo_codigo)
        
        if (len(titulo_nombre) <= nmax_nombres):
            n_caracteres[1] = nmax_nombres
        else:
            n_caracteres[1] = len(titulo_nombre)
        
        if (len(titulo_descripcion) <= nmax_descripciones):
            n_caracteres[2] = nmax_descripciones
        else:
            n_caracteres[2] = len(titulo_descripcion)

        if (len(titulo_cantidad) <= nmax_cantidades):
            n_caracteres[3] = nmax_cantidades
        else:
            n_caracteres[3] = len(titulo_cantidad)
        
        if (len(titulo_precio) <= nmax_precios):
            n_caracteres[4] = nmax_precios
        else:
            n_caracteres[4] = len(titulo_precio)
        
        if (len(titulo_categoria) <= nmax_categorias):
            n_caracteres[5] = nmax_categorias
        else:
            n_caracteres[5] = len(titulo_categoria)
        
        # Mostrar los registros en pantalla.
        print(f"\n{titulo_codigo}" + " " * (n_caracteres[0]-len(titulo_codigo)) 
            + f" {titulo_nombre}" + " " * (n_caracteres[1]-len(titulo_nombre)) 
            + f" {titulo_descripcion}" + " " * (n_caracteres[2]-len(titulo_descripcion)) 
            + f" {titulo_cantidad}"  + " " * (n_caracteres[3]-len(titulo_cantidad)) 
            + f" {titulo_precio}" + " " * (n_caracteres[4]-len(titulo_precio)) 
            + f" {titulo_categoria}" + " " * (n_caracteres[5]-len(titulo_categoria))
            )
        print(
            "=" * n_caracteres[0]
            + " "
            + "=" * n_caracteres[1]
            + " "
            + "=" * n_caracteres[2]
            + " "
            + "=" * n_caracteres[3]
            + " "
            + "=" * n_caracteres[4]
            + " "
            + "=" * n_caracteres[5]
            )
        for registro in resultados:
            codigo = registro[0]
            nombre = registro[1]
            descripcion = registro[2]
            cantidad = registro[3]
            precio = registro[4]
            categoria = registro[5]
            print(
                f"{codigo}"
                + " " * (n_caracteres[0]-len(str(codigo)))
                + " "
                + f"{nombre}"
                + " " * (n_caracteres[1]-len(nombre)) 
                + " "
                + f"{descripcion}"
                + " " * (n_caracteres[2]-len(descripcion))
                + " "
                + f"{cantidad}"
                + " " * (n_caracteres[3]-len(str(cantidad)))
                + " "
                + f"{precio}"
                + " " * (n_caracteres[4]-len(str(precio))) 
                + " "
                + f"{categoria}"
                + " " * (n_caracteres[5]-len(categoria)) 
                + " "
            )
    else:
        print(f"\nNo se encontró ningún producto.\n")

def buscar_por_codigo(codigo):
    cursor.execute(f"SELECT * FROM inventario where {campos[0]} = ?",(codigo,))
    return cursor.fetchall()

# Búsqueda de productos por nombre.
def buscar_producto(opcion_consultar):

    if opcion_consultar == 1:
        seguir = True
        while seguir:
            try:
                codigo = int(input("\nIngrese el código del producto a buscar: "))
            except:
                print(f"\nDebe ingresar un número.\n")
            else:
                resultado = buscar_por_codigo(codigo)
                seguir = False
    else:
        if opcion_consultar == 4:
            # Obtener todos los registros.
            cursor.execute("SELECT * FROM inventario")
        else:
            if opcion_consultar == 2:
                # Pedir al usuario el nombre del producto a buscar.
                buscar = input("\nIngrese el nombre o patrón de búsqueda (RegEx): ")
            elif opcion_consultar == 3:
                # Pedir al usuario el nombre del producto a buscar.
                buscar = input("\nIngrese la descripción o patrón de búsqueda (RegEx): ")
            # Obtener todos los registros.
            cursor.execute(f"SELECT * FROM inventario WHERE {campos[opcion_consultar-1]} LIKE '%{buscar}%'")
        
        resultado = cursor.fetchall()
    
    return resultado

def consultar_producto():

    titulo_menu_buscar = "Buscar un producto."
    titulo_menu_buscar_nombre = "Buscar producto por su nombre."
    titulo_menu_buscar_desc = "Buscar producto por su descripción."
    titulo_menu_buscar_codigo = "Buscar producto por su código."
    titulo_lista = "Lista de productos."
    
    continuar = True

    opciones = {
            1: "Buscar por código",
            2: "Buscar por nombre",
            3: "Buscar por descripción",
            4: "Mostrar todos los productos",
            5: "Volver al menú anterior"
        }
    
    opcion = 0

    while continuar:
        limpiar_pantalla()
        i = 1
        print()
        print("=" * len(titulo_menu_buscar))
        print(titulo_menu_buscar)
        print("=" * len(titulo_menu_buscar))
        print()
        for i in opciones.keys():
            print(f"{i}. {opciones[i]}.")

        # Solicitar al usuario que seleccione una opción
        try:
            opcion = int(input(f"\nPor favor, seleccione una opción (1-4): "))
        except:
            print(f"\nDebe ingresar un número entre 1 y 4 inclusive.")
        else:
            if (opcion == 5 ):
                continuar = False
            else:
                print()
                if opcion==1:
                    print("=" * len(titulo_menu_buscar_codigo))
                    print(titulo_menu_buscar_codigo)
                    print("=" * len(titulo_menu_buscar_codigo))
                elif opcion==2:
                    print("=" * len(titulo_menu_buscar_nombre))
                    print(titulo_menu_buscar_nombre)
                    print("=" * len(titulo_menu_buscar_nombre))
                elif opcion==3:
                    print("=" * len(titulo_menu_buscar_desc))
                    print(titulo_menu_buscar_desc)
                    print("=" * len(titulo_menu_buscar_desc))
                elif opcion == 4:
                    print("=" * len(titulo_lista))
                    print(titulo_lista)
                    print("=" * len(titulo_lista))

                resultado = buscar_producto(opcion)

                n = len(resultado)
                
                if opcion != 4: 
                    if n==1:
                        print(f"\n\tSe encontró un producto.")
                        print(f"\nDatos del producto encontrado:")
                    elif n>1:
                        print(f"\n\tSe encontraron {n} productos.")
                        print("\nDatos de los productos encontrados:")

                imprimir_resultados(resultado)

                continuar = (
                    input("\n¿Desea consultar otro producto? Ingrese 's' o '[n]': ").lower() == "s"
                )
                print()

def modificar_producto():

    titulo_modificar = "Modificar la información productos."
    titulo_menu_modificar_nombre = "Modificar producto por su nombre."
    titulo_menu_modificar_desc = "Modificar producto por su descripción."
    titulo_menu_modificar_codigo = "Modificar producto por su código."

    continuar = True

    opciones = {
            1: "Seleccionar producto a modificar por código",
            2: "Seleccionar producto a modificar por nombre",
            3: "Seleccionar producto a modificar por descripción",
            4: "Volver al menú principal"
        }
    
    opcion = 0

    while continuar:

        limpiar_pantalla()

        print()
        print("=" * len(titulo_modificar))
        print(titulo_modificar)
        print("=" * len(titulo_modificar))
        print()

        for i in opciones.keys():
            print(f"{i}. {opciones[i]}.")

        # Solicitar al usuario que seleccione una opción
        try:
            opcion = int(input(f"\nPor favor, seleccione una opción (1-4): "))
        except:
            print(f"\nDebe ingresar un número entre 1 y 4 inclusive.")
        else:
            if (opcion == 4):
                continuar = False
            else:
                seguir = True
                while seguir:
                    print()
                    if opcion == 1:
                        print("=" * len(titulo_menu_modificar_codigo))
                        print(titulo_menu_modificar_codigo)
                        print("=" * len(titulo_menu_modificar_codigo))
                        try:
                            codigo = int(input("\nIngrese el código del producto a modificar: "))
                        except:
                            print(f"\nDebe ingresar un número.\n")
                        else:
                            producto_a_modificar = buscar_por_codigo(codigo)
                            imprimir_resultados(producto_a_modificar)
                    else:
                        if opcion == 2:
                            print("=" * len(titulo_menu_modificar_nombre))
                            print(titulo_menu_modificar_nombre)
                            print("=" * len(titulo_menu_modificar_nombre))
                        elif opcion == 3:
                            print("=" * len(titulo_menu_modificar_desc))
                            print(titulo_menu_modificar_desc)
                            print("=" * len(titulo_menu_modificar_desc))

                        resultado = buscar_producto(opcion)
                        imprimir_resultados(resultado)
                        n = len(resultado)
                        if n>1:
                            try:
                                codigo = int(input("\nIngrese el código del producto a modificar: "))
                            except:
                                print(f"\nDebe ingresar un número.\n")
                            else:
                                producto_a_modificar = buscar_por_codigo(codigo)
                                imprimir_resultados(producto_a_modificar)
                        else:
                            codigo = resultado[0][0]
                        
                    confirmar = (
                                input("\n¿Confirma modificar este producto? Ingrese 's' o '[n]': ").lower() == "s"
                            )
                    
                    if confirmar:

                        cont = True
                        while cont:
                            print(" ")
                            for i in opciones_modificar.keys():
                                print(f"{i}. {opciones_modificar[i]}.")
                            
                            try:
                                opcion = int(input("\nPor favor, seleccione una opción (1-5): "))
                            except:
                                print("\nDebe ingresar un número entre 1 y 5.")

                            if opcion==1:
                                nuevo_valor = input("Ingrese el nuevo nombre del producto: ")
                            elif opcion==2:
                                nuevo_valor = input("Ingrese la nueva descripción: ")
                            elif opcion==3:
                                nuevo_valor = int(input("Ingrese el nuevo valor de la cantidad en stock: "))
                            elif opcion==4:
                                nuevo_valor = float(input("Ingrese el nuevo precio del producto: "))
                            elif opcion==5:
                                nuevo_valor = input("Ingrese el nuevo nombre de la categoría del producto: ")
                            
                            cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nuevo_valor,codigo))
                            
                            # Confirmar cambios.
                            conexion.commit()

                            # Producto modificado con éxito.
                            print(f"\nProducto modificado con éxito (código {codigo}).\n")

                            cont = (
                                input("\n¿Desea modificar otro campo? Ingrese 's' o '[n]': ").lower() == "s"
                            )
                            print(" ")

                    seguir = False
        # Preguntar al usuario si el usuario quiere eliminar otro producto.
        continuar = (
            input("\n¿Desea modificar otro producto? Ingrese 's' o '[n]': ").lower() == "s"
        )
        print(" ")

def eliminar_producto():

    titulo_eliminar = "Eliminar productos."
    titulo_menu_eliminar_nombre = "Eliminar producto por su nombre."
    titulo_menu_eliminar_desc = "Eliminar producto por su descripción."
    titulo_menu_eliminar_codigo = "Eliminar producto por su código."

    continuar = True

    opciones = {
            1: "Seleccionar producto a eliminar por código",
            2: "Seleccionar producto a eliminar por nombre",
            3: "Seleccionar producto a eliminar por descripción",
            4: "Volver al menú principal"
        }
    
    opcion = 0

    while continuar:

        limpiar_pantalla()

        print()
        print("=" * len(titulo_eliminar))
        print(titulo_eliminar)
        print("=" * len(titulo_eliminar))
        print()

        for i in opciones.keys():
            print(f"{i}. {opciones[i]}.")

        try:
            opcion = int(input(f"\nPor favor, seleccione una opción (1-4): "))
        except:
            print(f"\nDebe ingresar un número entero.")
        else:
            if (opcion == 4):
                continuar = False
            elif opcion in opciones.keys():
                seguir = True
                while seguir:
                    print()
                    if opcion == 1:
                        print("=" * len(titulo_menu_eliminar_codigo))
                        print(titulo_menu_eliminar_codigo)
                        print("=" * len(titulo_menu_eliminar_codigo))
                        try:
                            codigo = int(input("\nIngrese el código del producto a eliminar: "))
                        except:
                            print(f"\nDebe ingresar un número.\n")
                        else:
                            producto_a_eliminar = buscar_por_codigo(codigo)
                            imprimir_resultados(producto_a_eliminar)
                    else:
                        if opcion == 2:
                            print("=" * len(titulo_menu_eliminar_codigo))
                            print(titulo_menu_eliminar_codigo)
                            print("=" * len(titulo_menu_eliminar_codigo))
                        elif opcion == 3:
                            print("=" * len(titulo_menu_eliminar_codigo))
                            print(titulo_menu_eliminar_codigo)
                            print("=" * len(titulo_menu_eliminar_codigo))
                        
                        resultado = buscar_producto(opcion)
                        imprimir_resultados(resultado)
                        n = len(resultado)
                        if n>1:
                            try:
                                codigo = int(input("\nIngrese el código del producto a eliminar: "))
                            except:
                                print(f"\nDebe ingresar un número.\n")
                            else:
                                producto_a_eliminar = buscar_por_codigo(codigo)
                                imprimir_resultados(producto_a_eliminar)
                        else:
                            codigo = resultado[0][0]
                        
                    confirmar = (
                                input("\n¿Confirma eliminar este producto? Ingrese 's' o '[n]': ").lower() == "s"
                            )
                    if confirmar:
                        cursor.execute("DELETE FROM inventario where Código = ?",(codigo,))
                        # Confirmar cambios.
                        conexion.commit()

                        # Producto eliminado con éxito.
                        print(f"\nProducto eliminado con éxito (código {codigo}).\n")
                    seguir = False
            else:
                print("\nDebe ingresar un número entre 1 y 4, inclusive.")            

        # Preguntar al usuario si el usuario quiere eliminar otro producto.
        continuar = (
            input("\n¿Desea eliminar otro producto? Ingrese 's' o '[n]': ").lower() == "s"
        )
        print(" ")

def imprimir_menu_ppal():
    # Menú de opciones

    titulo_menu_ppal = "Sistema de gestión de productos."

    limpiar_pantalla()
    print()
    print("=" * len(titulo_menu_ppal))
    print(titulo_menu_ppal)
    print("=" * len(titulo_menu_ppal))
    print()
    for opt in opciones_menu_ppal.keys():
        print(f"{opt}. {opciones_menu_ppal[opt]}.")

# Programa principal.

def menu_principal():
    
    opcion = 0

    opcion_salir = int(list(opciones_menu_ppal.keys())[list(opciones_menu_ppal.values()).index("Salir")])
    while opcion != opcion_salir:

        imprimir_menu_ppal()

        # Solicitar al usuario que seleccione una opción
        try:
            opcion = int(input(f"\nPor favor, seleccione una opción (1-{opcion_salir}): "))
        except:
            print(f"\nDebe ingresar un número entre 1 y {opcion_salir}, inclusive.")
        else:
            if opcion == 1:
                agregar_producto()
            elif opcion == 2:
                consultar_producto()
            elif opcion == 3:
                modificar_producto()
            elif opcion == 4:
                eliminar_producto()
            elif opcion == opcion_salir:
                print("\n\t¡Gracias por utlizar nuestro sistema!\n\n\t¡Hasta pronto!\n")
                conexion.close()