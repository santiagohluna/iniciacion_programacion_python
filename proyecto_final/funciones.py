import os
import re
import sqlite3
import numpy as np

titulo_menu_ppal = "Menú de gestión de productos."
titulo_menu_buscar = "Buscar un producto."
titulo_menu_buscar_nombre = "Buscar producto por su nombre."
titulo_menu_buscar_desc = "Buscar producto por su descripción."
titulo_menu_buscar_codigo = "Buscar producto por su código."
titulo_menu_eliminar_nombre = "Eliminar producto por su nombre."
titulo_menu_eliminar_desc = "Eliminar producto por su descripción."
titulo_menu_eliminar_codigo = "Eliminar producto por su código."
titulo_menu_modificar_nombre = "Modificar producto por su nombre."
titulo_menu_modificar_desc = "Modificar producto por su descripción."
titulo_menu_modificar_codigo = "Modificar producto por su código."
titulo_menu_buscar = "Buscar un producto."
titulo_eliminar = "Eliminar un producto."
titulo_modificar = "Modificar la información de un producto."
titulo_registro = "Alta de productos"
titulo_codigo = "Código"
titulo_nombre = "Nombre del producto"
titulo_descripcion = "Descripción"
titulo_precio = "Precio" + " " * 10
titulo_cantidad = "Cantidad en stock"
titulo_categoria = "Categoría"
titulo_lista = "Lista de productos."

inventario = []

n_caracteres = [0,0,0,0,0,0]

opciones_modificar = {1: "Modificar el nombre del producto",
            2: "Modificar la descripción del producto",
            3: "Modificar la cantidad en stock",
            4: "Modificar el precio del producto",
            5: "Modificar la categoría del producto"
            }

campos = {1: "Nombre",
            2: "Descripción",
            3: "Cantidad",
            4: "Precio",
            5: "Categoría"}

# Limpiar pantalla
def limpiar_pantalla():
    os.system("clear")

# Función para agregar productos.
def agregar_producto():
    # Crear la conexión a la base de datos.
    conexion = sqlite3.connect("PFI_Python.db")
    cursor = conexion.cursor()

    limpiar_pantalla()
    print(" ")
    print(titulo_registro)
    print("=" * len(titulo_registro))
    print(" ")
    continuar = True
    while continuar:
        # Ingresar los datos del producto a agregar.
        try:
            codigo = int(input("Ingrese el código del producto (enter para volver al menú principal): "))
        except:
            codigo = -1
        else:
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese una descripción del producto: ")
            cantidad = int(input("Ingrese la cantidad en stock: "))
            precio = float(input("Ingrese el precio del producto: "))
            categoria = input("Ingrese la categoría del producto: ")

            # Agregar el producto a la base de datos.
            cursor.execute("INSERT INTO inventario(Código, Nombre, Descripción, Cantidad, Precio, Categoría) VALUES (?, ?, ?, ?, ?, ?)",(codigo,nombre,descripcion,cantidad,precio,categoria))

            # Confirmar cambios.
            conexion.commit()

            # Producto registrado con éxito.
            print(f"\nProducto registrado con el código {codigo}.\n")

        # Preguntar al usuario si quiere agregar otro producto.
        if codigo < 0:
            break
        else:
            continuar = (
                input("¿Desea agregar otro producto? Ingrese 's' o '[n]': ").lower() == "s"
            )
            print(" ")

    # Cerrar la conexión
    conexion.close()

# Búsqueda de productos por código.
def buscar_por_codigo():
    # Crear la conexión a la base de datos.
    conexion = sqlite3.connect("PFI_Python.db")
    cursor = conexion.cursor()

    continuar = True

    while continuar:

        print()
        print("=" * len(titulo_menu_buscar_codigo))
        print(titulo_menu_buscar_codigo)
        print("=" * len(titulo_menu_buscar_codigo))
        print()
        
        try:
            codigo = int(input("Ingrese el código del producto a buscar: "))
        except:
            print(f"\nDebe ingresar un número.\n")
        else:
            cursor.execute("SELECT * FROM inventario where Código = ?",(codigo,))
            resultado = cursor.fetchone()
            
            # Verificar si se encontró el registro.
            if resultado:
                print("\nDatos del producto consultado:\n")
                print(f"\tCódigo: {resultado[0]}.")
                print(f"\tNombre: {resultado[1]}.")
                print(f"\tDescripción: {resultado[2]}.")
                print(f"\tCantidad: {resultado[3]} unidades.")
                print(f"\tPrecio: $ {resultado[4]}.")
                print(f"\tCategoría: {resultado[5]}.")
            else:
                print(f"\nNo se encontró el producto con el código {codigo}.")

        continuar = (
            input("\n¿Desea consultar otro producto por código? Ingrese 's' o '[n]': ").lower() == "s"
        )

        # Cerrar la conexión
        conexion.close()
    
# Búsqueda de productos por nombre.
def buscar_por_nombre():

    # Crear la conexión a la base de datos.
    conexion = sqlite3.connect("PFI_Python.db")
    cursor = conexion.cursor()

    continuar = True

    while continuar:
        
        limpiar_pantalla()

        print()
        print("=" * len(titulo_menu_buscar_nombre))
        print(titulo_menu_buscar_nombre)
        print("=" * len(titulo_menu_buscar_nombre))
        print()

        # Obtener todos los registros.
        cursor.execute("SELECT * FROM inventario")
        inventario = cursor.fetchall()

        # Pedir al usuario el nombre del producto a buscar.
        txt = input("Ingrese el nombre o patrón de búsqueda (RegEx): ")

        resultados = {}

        n = 0

        if inventario:
            for registro in inventario:
                x = re.search(txt,registro[1], re.IGNORECASE)
                if x:
                    resultados[n] = registro
                    n += 1
        else:
            print("\nEl inventario está vacío.")

        if n==1:
            print("\n\tSe encontró un producto con el nombre ingresado.\n")
        elif n>1:
            print(f"\n\tSe encontraron {n} productos con el nombre ingresado.\n")
        
        if resultados:
            for i in resultados:
                resultado = resultados[i]
                print(f"\nDatos del producto {i+1} encontrado:\n")
                print(f"\tCódigo: {resultado[0]}.")
                print(f"\tNombre: {resultado[1]}.")
                print(f"\tDescripción: {resultado[2]}.")
                print(f"\tCantidad: {resultado[3]} unidades.")
                print(f"\tPrecio: $ {resultado[4]}.")
                print(f"\tCategoría: {resultado[5]}.")
                n += 1
        else:
            print("\nNo se encontró ningún producto con ese nombre.")

        print(" ")
        continuar = (
            input("¿Desea consultar otro producto por nombre? Ingrese 's' o '[n]': ").lower() == "s"
        )

    # Cerrar la conexión
    conexion.close()

def buscar_por_descripcion():

     # Crear la conexión a la base de datos.
    conexion = sqlite3.connect("PFI_Python.db")
    cursor = conexion.cursor()

    continuar = True

    while continuar:
        
        limpiar_pantalla()

        print()
        print("=" * len(titulo_menu_buscar_desc))
        print(titulo_menu_buscar_desc)
        print("=" * len(titulo_menu_buscar_desc))
        print()

        # Obtener todos los registros.
        cursor.execute("SELECT * FROM inventario")
        inventario = cursor.fetchall()

        # Pedir al usuario el nombre del producto a buscar.
        txt = input("Ingrese la descripción o patrón de búsqueda (RegEx): ")

        resultados = {}

        n = 0

        if inventario:
            for registro in inventario:
                x = re.search(txt,registro[2], re.IGNORECASE)
                if x:
                    resultados[n] = registro
                    n += 1
        else:
            print("\nEl inventario está vacío.")

        if n==1:
            print("\n\tSe encontró un producto con la descripción ingresada.\n")
        elif n>1:
            print(f"\n\tSe encontraron {n} productos con la descripción ingresada.\n")
        
        if resultados:
            for i in resultados:
                resultado = resultados[i]
                print(f"\nDatos del producto {i+1} encontrado:\n")
                print(f"\tCódigo: {resultado[0]}.")
                print(f"\tNombre: {resultado[1]}.")
                print(f"\tDescripción: {resultado[2]}.")
                print(f"\tCantidad: {resultado[3]} unidades.")
                print(f"\tPrecio: $ {resultado[4]}.")
                print(f"\tCategoría: {resultado[5]}.")
                n += 1
        else:
            print("\nNo se encontró ningún producto con esa descripción.")

        print(" ")
        continuar = (
            input("¿Desea consultar otro producto por descripción? Ingrese 's' o '[n]': ").lower() == "s"
        )

    # Cerrar la conexión
    conexion.close()

def buscar_producto():
    
    continuar = True

    opciones = {
            1: "Buscar por código",
            2: "Buscar por nombre",
            3: "Buscar por descripción",
            4: "Volver al menú anterior"
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
        for opt in opciones:
            print(f"{i}. {opciones[i]}.")
            i += 1

        # Solicitar al usuario que seleccione una opción
        while (opcion != 1 or 2 or 3 or 4):
            try:
                opcion = int(input(f"\nPor favor, seleccione una opción (1-4): "))
            except:
                print(f"\nDebe ingresar un número.")
            else:
                if opcion == 1:
                    buscar_por_codigo()
                    break
                elif opcion == 2:
                    buscar_por_nombre()
                    break
                elif opcion == 3:
                    buscar_por_descripcion()
                    break
                elif opcion == 4:
                    break
                else:
                    print(f"\nDebe ingresar un número entre 1 y 4 inclusive.")
                    continue
        
        if (opcion == 4 ):
            continuar = False
        else:
            continuar = (
                input("¿Desea consultar otro producto? Ingrese 's' o '[n]': ").lower() == "s"
            )
            print(" ")

def modificar_por_codigo():
    # Crear la conexión a la base de datos.
    conexion = sqlite3.connect("PFI_Python.db")
    cursor = conexion.cursor()

    continuar = True

    while continuar:

        print()
        print("=" * len(titulo_menu_eliminar_codigo))
        print(titulo_menu_eliminar_codigo)
        print("=" * len(titulo_menu_eliminar_codigo))
        print()
        
        codigo = -1

        while codigo < 0:
            try:
                codigo = int(input("Ingrese el código del producto a modificar: "))
            except:
                print(f"\nDebe ingresar un número.\n")
                codigo = -1
            else:
                try:
                    cursor.execute("SELECT * FROM inventario where Código = ?",(codigo,))
                    resultado = cursor.fetchone()
                except:
                    print(f"\nNo se encontró el producto con el código {codigo}.")
                    codigo = -1
                else:
                # Verificar si se encontró el registro.
                    if resultado:
                        print("\nDatos del producto a modificar:\n")
                        print(f"\tCódigo: {resultado[0]}.")
                        print(f"\tNombre: {resultado[1]}.")
                        print(f"\tDescripción: {resultado[2]}.")
                        print(f"\tCantidad: {resultado[3]} unidades.")
                        print(f"\tPrecio: $ {resultado[4]}.")
                        print(f"\tCategoría: {resultado[5]}.")

                        confirmar = (
                            input("\n¿Confirma modificar este producto? Ingrese 's' o '[n]': ").lower() == "s"
                        )
                        if confirmar:
                            i = 1
                            print(" ")
                            for opt in opciones_modificar:
                                print(f"{i}. {opciones_modificar[i]}.")
                                i += 1
                            
                            try:
                                opcion = int(input("\nPor favor, seleccione una opción (1-5): "))
                            except:
                                print("\nDebe ingresar un número entre 1 y 6.")

                            if opcion==1:
                                nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
                                cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nuevo_nombre,codigo))
                            elif opcion==2:
                                nueva_desc = input("Ingrese la nueva descricpción: ")
                                cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nueva_desc,codigo))
                            elif opcion==3:
                                nueva_cantidad = int(input("Ingrese el nuevo valor de la cantidad en stock: "))
                                cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nueva_cantidad,codigo))
                            elif opcion==4:
                                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                                cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nuevo_precio,codigo))
                            elif opcion==5:
                                nueva_categoria = input("Ingrese el nuevo nombre de la categoría del producto: ")
                                cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nueva_categoria,codigo))
                            
                            # Confirmar cambios.
                            conexion.commit()

                            # Producto eliminado con éxito.
                            print(f"\nProducto modificado con éxito (código {codigo}).\n")

        continuar = (
            input("\n¿Desea modificar otro producto por código? Ingrese 's' o '[n]': ").lower() == "s"
        )

    # Cerrar la conexión
    conexion.close()

# Modificar productos por nombre.
def modificar_por_nombre():

    # Crear la conexión a la base de datos.
    conexion = sqlite3.connect("PFI_Python.db")
    cursor = conexion.cursor()

    continuar = True

    while continuar:
        
        limpiar_pantalla()

        print()
        print("=" * len(titulo_menu_modificar_nombre))
        print(titulo_menu_modificar_nombre)
        print("=" * len(titulo_menu_modificar_nombre))
        print()

        # Obtener todos los registros.
        cursor.execute("SELECT * FROM inventario")
        inventario = cursor.fetchall()

        # Pedir al usuario el nombre del producto a buscar.
        txt = input("Ingrese el nombre o patrón de búsqueda (RegEx): ")

        resultados = {}

        n = 0

        if inventario:
            for registro in inventario:
                x = re.search(txt,registro[1], re.IGNORECASE)
                if x:
                    resultados[n] = registro
                    n += 1
        else:
            print("\nEl inventario está vacío.")

        if resultados:
            if n==1:
                print("\n\tSe encontró un producto con el nombre ingresado.\n")
                resultado = resultados[0]
                print(f"\nDatos del producto encontrado:\n")
                print(f"\tCódigo: {resultado[0]}.")
                print(f"\tNombre: {resultado[1]}.")
                print(f"\tDescripción: {resultado[2]}.")
                print(f"\tCantidad: {resultado[3]} unidades.")
                print(f"\tPrecio: ${resultado[4]}.")
                print(f"\tCategoría: {resultado[5]}.")
            elif n>1:
                print(f"\n\tSe encontraron {n} productos con el nombre ingresado.\n")
                for i in resultados:
                    resultado = resultados[i]
                    print(f"\nDatos del producto {i+1} encontrado:\n")
                    print(f"\tCódigo: {resultado[0]}.")
                    print(f"\tNombre: {resultado[1]}.")
                    print(f"\tDescripción: {resultado[2]}.")
                    print(f"\tCantidad: {resultado[3]} unidades.")
                    print(f"\tPrecio: ${resultado[4]}.")
                    print(f"\tCategoría: {resultado[5]}.")
                    n += 1
            
            codigo = -1

            while codigo < 0:
                try:
                    if n>1:
                        codigo = int(input("\nIngrese el código del producto a modificar: "))
                    else:
                        codigo = resultado[0]
                except:
                    print(f"\nDebe ingresar un número.\n")
                    codigo = -1
                else:
                    try:
                        cursor.execute("SELECT * FROM inventario where Código = ?",(codigo,))
                        resultado = cursor.fetchone()
                    except:
                        print(f"\nNo se encontró el producto con el código {codigo}.")
                        codigo = -1
                    else:
                    
                        if n>1:
                            # Verificar si se encontró el registro.
                            if resultado:
                                print("\nDatos del producto a modificar:\n")
                                print(f"\tCódigo: {resultado[0]}.")
                                print(f"\tNombre: {resultado[1]}.")
                                print(f"\tDescripción: {resultado[2]}.")
                                print(f"\tCantidad: {resultado[3]} unidades.")
                                print(f"\tPrecio: $ {resultado[4]}.")
                                print(f"\tCategoría: {resultado[5]}.")

                        confirmar = (
                            input("\n¿Confirma modificar este producto? Ingrese 's' o '[n]': ").lower() == "s"
                        )
                        if confirmar:
                                
                            i = 1
                            print(" ")
                            for opt in opciones_modificar:
                                print(f"{i}. {opciones_modificar[i]}.")
                                i += 1
                            
                            try:
                                opcion = int(input("\nPor favor, seleccione una opción (1-5): "))
                            except:
                                print("\nDebe ingresar un número entre 1 y 6.")

                            if opcion==1:
                                nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
                                cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nuevo_nombre,codigo))
                            elif opcion==2:
                                nueva_desc = input("Ingrese la nueva descricpción: ")
                                cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nueva_desc,codigo))
                            elif opcion==3:
                                nueva_cantidad = int(input("Ingrese el nuevo valor de la cantidad en stock: "))
                                cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nueva_cantidad,codigo))
                            elif opcion==4:
                                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                                cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nuevo_precio,codigo))
                            elif opcion==5:
                                nueva_categoria = input("Ingrese el nuevo nombre de la categoría del producto: ")
                                cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nueva_categoria,codigo))
                            
                            # Confirmar cambios.
                            conexion.commit()

                            # Producto modificado con éxito.
                            print(f"\nProducto modificado con éxito (código {codigo}).\n")

        print(" ")
        continuar = (
            input("¿Desea modificar otro producto por nombre? Ingrese 's' o '[n]': ").lower() == "s"
        )

    # Cerrar la conexión
    conexion.close()

# MOdificar producto por su descripción.
def modificar_por_descripcion():
    
    # Crear la conexión a la base de datos.
    conexion = sqlite3.connect("PFI_Python.db")
    cursor = conexion.cursor()

    continuar = True

    while continuar:
        
        limpiar_pantalla()

        print()
        print("=" * len(titulo_menu_modificar_desc))
        print(titulo_menu_modificar_desc)
        print("=" * len(titulo_menu_modificar_desc))
        print()

        # Obtener todos los registros.
        cursor.execute("SELECT * FROM inventario")
        inventario = cursor.fetchall()

        # Pedir al usuario la descripción del producto a eliminar.
        txt = input("Ingrese la descripción o patrón de búsqueda (RegEx): ")

        resultados = {}

        n = 0

        if inventario:
            for registro in inventario:
                x = re.search(txt,registro[2], re.IGNORECASE)
                if x:
                    resultados[n] = registro
                    n += 1
        else:
            print("\nEl inventario está vacío.")

        if resultados:
            if n==1:
                print("\n\tSe encontró un producto con el nombre ingresado.\n")
                resultado = resultados[0]
                print(f"\nDatos del producto encontrado:\n")
                print(f"\tCódigo: {resultado[0]}.")
                print(f"\tNombre: {resultado[1]}.")
                print(f"\tDescripción: {resultado[2]}.")
                print(f"\tCantidad: {resultado[3]} unidades.")
                print(f"\tPrecio: ${resultado[4]}.")
                print(f"\tCategoría: {resultado[5]}.")
            elif n>1:
                print(f"\n\tSe encontraron {n} productos con el nombre ingresado.\n")
                for i in resultados:
                    resultado = resultados[i]
                    print(f"\nDatos del producto {i+1} encontrado:\n")
                    print(f"\tCódigo: {resultado[0]}.")
                    print(f"\tNombre: {resultado[1]}.")
                    print(f"\tDescripción: {resultado[2]}.")
                    print(f"\tCantidad: {resultado[3]} unidades.")
                    print(f"\tPrecio: ${resultado[4]}.")
                    print(f"\tCategoría: {resultado[5]}.")
                    n += 1
            
            codigo = -1

            while codigo < 0:
                try:
                    if n>1:
                        codigo = int(input("\nIngrese el código del producto a modificar: "))
                    else:
                        codigo = resultado[0]
                except:
                    print(f"\nDebe ingresar un número.\n")
                    codigo = -1
                else:
                    try:
                        cursor.execute("SELECT * FROM inventario where Código = ?",(codigo,))
                        resultado = cursor.fetchone()
                    except:
                        print(f"\nNo se encontró el producto con el código {codigo}.")
                        codigo = -1
                    else:
                    
                        if n>1:
                            # Verificar si se encontró el registro.
                            if resultado:
                                print("\nDatos del producto a modificar:\n")
                                print(f"\tCódigo: {resultado[0]}.")
                                print(f"\tNombre: {resultado[1]}.")
                                print(f"\tDescripción: {resultado[2]}.")
                                print(f"\tCantidad: {resultado[3]} unidades.")
                                print(f"\tPrecio: $ {resultado[4]}.")
                                print(f"\tCategoría: {resultado[5]}.")

                        confirmar = (
                            input("\n¿Confirma modificar este producto? Ingrese 's' o '[n]': ").lower() == "s"
                        )
                        if confirmar:
                            
                            i = 1
                            print(" ")
                            for opt in opciones_modificar:
                                print(f"{i}. {opciones_modificar[i]}.")
                                i += 1
                            
                            try:
                                opcion = int(input("\nPor favor, seleccione una opción (1-5): "))
                            except:
                                print("\nDebe ingresar un número entre 1 y 6.")

                            if opcion==1:
                                nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
                                cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nuevo_nombre,codigo))
                            elif opcion==2:
                                nueva_desc = input("Ingrese la nueva descricpción: ")
                                cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nueva_desc,codigo))
                            elif opcion==3:
                                nueva_cantidad = int(input("Ingrese el nuevo valor de la cantidad en stock: "))
                                cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nueva_cantidad,codigo))
                            elif opcion==4:
                                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                                cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nuevo_precio,codigo))
                            elif opcion==5:
                                nueva_categoria = input("Ingrese el nuevo nombre de la categoría del producto: ")
                                cursor.execute(f"UPDATE inventario SET {campos[opcion]} = ? where Código = ?",(nueva_categoria,codigo))
                            
                            # Confirmar cambios.
                            conexion.commit()

                            # Producto registrado con éxito.
                            print(f"\nProducto modificado con éxito (código {codigo}).\n")

        print(" ")
        continuar = (
            input("¿Desea modificar otro producto por descripción? Ingrese 's' o '[n]': ").lower() == "s"
        )

    # Cerrar la conexión
    conexion.close()

def modificar_producto():

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

        i = 1
        for opt in opciones:
            print(f"{i}. {opciones[i]}.")
            i += 1

        # Solicitar al usuario que seleccione una opción
        while (opcion != 1 or 2 or 3 or 4):
            try:
                opcion = int(input(f"\nPor favor, seleccione una opción (1-4): "))
            except:
                print(f"Debe ingresar un número entre 1 y 3 inclusive.")
            else:
                if opcion == 1:
                    modificar_por_codigo()
                    break
                elif opcion == 2:
                    modificar_por_nombre()
                    break
                elif opcion == 3:
                    modificar_por_descripcion()
                    break
                elif opcion == 4:
                    break
                else:
                    print(f"\nDebe ingresar un número entre 1 y 3 inclusive.")
                    continue

        if opcion == 4:
            continuar = False
        else:
            # Preguntar al usuario si el usuario quiere eliminar otro producto.
            continuar = (
                input("\n¿Desea modificar otro producto? Ingrese 's' o '[n]': ").lower() == "s"
            )
            print(" ")

# Búsqueda de productos por código.
def eliminar_por_codigo():
    # Crear la conexión a la base de datos.
    conexion = sqlite3.connect("PFI_Python.db")
    cursor = conexion.cursor()

    continuar = True

    while continuar:

        print()
        print("=" * len(titulo_menu_eliminar_codigo))
        print(titulo_menu_eliminar_codigo)
        print("=" * len(titulo_menu_eliminar_codigo))
        print()
        
        codigo = -1

        while codigo < 0:
            try:
                codigo = int(input("Ingrese el código del producto a eliminar: "))
            except:
                print(f"\nDebe ingresar un número.\n")
                codigo = -1
            else:
                try:
                    cursor.execute("SELECT * FROM inventario where Código = ?",(codigo,))
                    resultado = cursor.fetchone()
                except:
                    print(f"\nNo se encontró el producto con el código {codigo}.")
                    codigo = -1
                else:
                
                    # Verificar si se encontró el registro.
                    if resultado:
                        print("\nDatos del producto a eliminar:\n")
                        print(f"\tCódigo: {resultado[0]}.")
                        print(f"\tNombre: {resultado[1]}.")
                        print(f"\tDescripción: {resultado[2]}.")
                        print(f"\tCantidad: {resultado[3]} unidades.")
                        print(f"\tPrecio: $ {resultado[4]}.")
                        print(f"\tCategoría: {resultado[5]}.")

                        confirmar = (
                            input("\n¿Confirma eliminar este producto? Ingrese 's' o '[n]': ").lower() == "s"
                        )
                        if confirmar:
                            cursor.execute("DELETE FROM inventario where Código = ?",(codigo,))
                            # Confirmar cambios.
                            conexion.commit()

                            # Producto eliminado con éxito.
                            print(f"\nProducto eliminado con éxito (código {codigo}).\n")

        continuar = (
            input("\n¿Desea eliminar otro producto por código? Ingrese 's' o '[n]': ").lower() == "s"
        )

    # Cerrar la conexión
    conexion.close()

# Eliminar productos por nombre.
def eliminar_por_nombre():

    # Crear la conexión a la base de datos.
    conexion = sqlite3.connect("PFI_Python.db")
    cursor = conexion.cursor()

    continuar = True

    while continuar:
        
        limpiar_pantalla()

        print()
        print("=" * len(titulo_menu_eliminar_nombre))
        print(titulo_menu_eliminar_nombre)
        print("=" * len(titulo_menu_eliminar_nombre))
        print()

        # Obtener todos los registros.
        cursor.execute("SELECT * FROM inventario")
        inventario = cursor.fetchall()

        # Pedir al usuario el nombre del producto a buscar.
        txt = input("Ingrese el nombre o patrón de búsqueda (RegEx): ")

        resultados = {}

        n = 0

        if inventario:
            for registro in inventario:
                x = re.search(txt,registro[1], re.IGNORECASE)
                if x:
                    resultados[n] = registro
                    n += 1
        else:
            print("\nEl inventario está vacío.")
        
        if resultados:
            if n==1:
                print("\n\tSe encontró un producto con el nombre ingresado.\n")
                resultado = resultados[0]
                print(f"\nDatos del producto encontrado:\n")
                print(f"\tCódigo: {resultado[0]}.")
                print(f"\tNombre: {resultado[1]}.")
                print(f"\tDescripción: {resultado[2]}.")
                print(f"\tCantidad: {resultado[3]} unidades.")
                print(f"\tPrecio: ${resultado[4]}.")
                print(f"\tCategoría: {resultado[5]}.")
            elif n>1:
                print(f"\n\tSe encontraron {n} productos con el nombre ingresado.\n")
                for i in resultados:
                    resultado = resultados[i]
                    print(f"\nDatos del producto {i+1} encontrado:\n")
                    print(f"\tCódigo: {resultado[0]}.")
                    print(f"\tNombre: {resultado[1]}.")
                    print(f"\tDescripción: {resultado[2]}.")
                    print(f"\tCantidad: {resultado[3]} unidades.")
                    print(f"\tPrecio: ${resultado[4]}.")
                    print(f"\tCategoría: {resultado[5]}.")
                    n += 1
            
            codigo = -1

            while codigo < 0:
                try:
                    if n>1:
                        codigo = int(input("\nIngrese el código del producto a modificar: "))
                    else:
                        codigo = resultado[0]
                except:
                    print(f"\nDebe ingresar un número.\n")
                    codigo = -1
                else:
                    try:
                        cursor.execute("SELECT * FROM inventario where Código = ?",(codigo,))
                        resultado = cursor.fetchone()
                    except:
                        print(f"\nNo se encontró el producto con el código {codigo}.")
                        codigo = -1
                    else:
                    
                        if n>1:
                        # Verificar si se encontró el registro.
                            if resultado:
                                print("\nDatos del producto a eliminar:\n")
                                print(f"\tCódigo: {resultado[0]}.")
                                print(f"\tNombre: {resultado[1]}.")
                                print(f"\tDescripción: {resultado[2]}.")
                                print(f"\tCantidad: {resultado[3]} unidades.")
                                print(f"\tPrecio: $ {resultado[4]}.")
                                print(f"\tCategoría: {resultado[5]}.")

                        confirmar = (
                            input("\n¿Confirma eliminar este producto? Ingrese 's' o '[n]': ").lower() == "s"
                        )
                        if confirmar:
                            cursor.execute("DELETE FROM inventario where Código = ?",(codigo,))
                            # Confirmar cambios.
                            conexion.commit()

                            # Producto registrado con éxito.
                            print(f"\nProducto eliminado con éxito (código {codigo}).\n")

        print(" ")
        continuar = (
            input("¿Desea eliminar otro producto por nombre? Ingrese 's' o '[n]': ").lower() == "s"
        )

    # Cerrar la conexión
    conexion.close()

# Eliminar producto por su descripción.
def eliminar_por_descripcion():
    
    # Crear la conexión a la base de datos.
    conexion = sqlite3.connect("PFI_Python.db")
    cursor = conexion.cursor()

    continuar = True

    while continuar:
        
        limpiar_pantalla()

        print()
        print("=" * len(titulo_menu_eliminar_nombre))
        print(titulo_menu_eliminar_nombre)
        print("=" * len(titulo_menu_eliminar_nombre))
        print()

        # Obtener todos los registros.
        cursor.execute("SELECT * FROM inventario")
        inventario = cursor.fetchall()

        # Pedir al usuario la descripción del producto a eliminar.
        txt = input("Ingrese la descripción o patrón de búsqueda (RegEx): ")

        resultados = {}

        n = 0

        if inventario:
            for registro in inventario:
                x = re.search(txt,registro[2], re.IGNORECASE)
                if x:
                    resultados[n] = registro
                    n += 1
        else:
            print("\nEl inventario está vacío.")

        if resultados:
            if n==1:
                print("\n\tSe encontró un producto con el nombre ingresado.\n")
                resultado = resultados[0]
                print(f"\nDatos del producto encontrado:\n")
                print(f"\tCódigo: {resultado[0]}.")
                print(f"\tNombre: {resultado[1]}.")
                print(f"\tDescripción: {resultado[2]}.")
                print(f"\tCantidad: {resultado[3]} unidades.")
                print(f"\tPrecio: ${resultado[4]}.")
                print(f"\tCategoría: {resultado[5]}.")
            elif n>1:
                print(f"\n\tSe encontraron {n} productos con el nombre ingresado.\n")
                for i in resultados:
                    resultado = resultados[i]
                    print(f"\nDatos del producto {i+1} encontrado:\n")
                    print(f"\tCódigo: {resultado[0]}.")
                    print(f"\tNombre: {resultado[1]}.")
                    print(f"\tDescripción: {resultado[2]}.")
                    print(f"\tCantidad: {resultado[3]} unidades.")
                    print(f"\tPrecio: ${resultado[4]}.")
                    print(f"\tCategoría: {resultado[5]}.")
                    n += 1
            
            codigo = -1

            while codigo < 0:
                try:
                    if n>1:
                        codigo = int(input("\nIngrese el código del producto a modificar: "))
                    else:
                        codigo = resultado[0]
                except:
                    print(f"\nDebe ingresar un número.\n")
                    codigo = -1
                else:
                    try:
                        cursor.execute("SELECT * FROM inventario where Código = ?",(codigo,))
                        resultado = cursor.fetchone()
                    except:
                        print(f"\nNo se encontró el producto con el código {codigo}.")
                        codigo = -1
                    else:
                    
                        if n>1:
                            # Verificar si se encontró el registro.
                            if resultado:
                                print("\nDatos del producto a eliminar:\n")
                                print(f"\tCódigo: {resultado[0]}.")
                                print(f"\tNombre: {resultado[1]}.")
                                print(f"\tDescripción: {resultado[2]}.")
                                print(f"\tCantidad: {resultado[3]} unidades.")
                                print(f"\tPrecio: $ {resultado[4]}.")
                                print(f"\tCategoría: {resultado[5]}.")

                            confirmar = (
                                input("\n¿Confirma eliminar este producto? Ingrese 's' o '[n]': ").lower() == "s"
                            )
                            if confirmar:
                                cursor.execute("DELETE FROM inventario where Código = ?",(codigo,))
                                # Confirmar cambios.
                                conexion.commit()

                                # Producto registrado con éxito.
                                print(f"\nProducto eliminado con éxito (código {codigo}).\n")

        print(" ")
        continuar = (
            input("¿Desea eliminar otro producto por descripción? Ingrese 's' o '[n]': ").lower() == "s"
        )

    # Cerrar la conexión
    conexion.close()
    

def eliminar_producto():

    limpiar_pantalla()

    continuar = True

    opciones = {
            1: "Seleccionar producto a eliminar por código",
            2: "Seleccionar producto a eliminar por nombre",
            3: "Seleccionar producto a eliminar por descripción",
            4: "Volver al menú principal"
        }
    
    opcion = 0

    while continuar:

        print()
        print("=" * len(titulo_eliminar))
        print(titulo_eliminar)
        print("=" * len(titulo_eliminar))
        print()

        i = 1
        for opt in opciones:
            print(f"{i}. {opciones[i]}.")
            i += 1

        # Solicitar al usuario que seleccione una opción
        while (opcion != 1 or 2 or 3 or 4):
            try:
                opcion = int(input(f"\nPor favor, seleccione una opción (1-4): "))
            except:
                print(f"Debe ingresar un número entre 1 y 3 inclusive.")
            else:
                if opcion == 1:
                    eliminar_por_codigo()
                    break
                elif opcion == 2:
                    eliminar_por_nombre()
                    break
                elif opcion == 3:
                    eliminar_por_descripcion()
                    break
                elif opcion == 4:
                    break
                else:
                    print(f"\nDebe ingresar un número entre 1 y 3 inclusive.")
                    continue

        if opcion == 4:
            continuar = False
        else:
            # Preguntar al usuario si el usuario quiere eliminar otro producto.
            continuar = (
                input("\n¿Desea eliminar otro producto? Ingrese 's' o '[n]': ").lower() == "s"
            )
            print(" ")
        


def consultar_inventario():
    limpiar_pantalla()

    # Crear la conexión a la base de datos.
    conexion = sqlite3.connect("PFI_Python.db")
    cursor = conexion.cursor()

    # Obtener todos los registros.
    cursor.execute("SELECT * FROM inventario")
    inventario = cursor.fetchall()

    n_codigos = []
    n_nombres = []
    n_descripciones = []
    n_cantidades = []
    n_precios = []
    n_categorias = []

    for registro in inventario:
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
    continuar = True
    while continuar:
        print(" ")
        print("=" * len(titulo_lista))
        print(titulo_lista)
        print("=" * len(titulo_lista))
        print(" ")
        
        print(f"{titulo_codigo}" + " " * (n_caracteres[0]-len(titulo_codigo)) 
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
        for registro in inventario:
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

        continuar = (
            input("\n\tPulse una tecla para volver al menú principal.\n").lower() == " "
        )

# Programa principal.

def menu_principal():

    # Menú de opciones

    opciones = {
        1: "Alta de productos nuevos",
        2: "Consulta de datos de productos",
        3: "Modificar la información de un producto",
        4: "Dar de baja productos",
        5: "Listado completo de productos",
        6: "Salir",
    }
    
    opcion = 0

    opcion_salir = int(list(opciones.keys())[list(opciones.values()).index("Salir")])
    while opcion != opcion_salir:
        limpiar_pantalla()
        i = 1
        print()
        print("=" * len(titulo_menu_ppal))
        print(titulo_menu_ppal)
        print("=" * len(titulo_menu_ppal))
        print()
        for opt in opciones:
            print(f"{i}. {opciones[i]}.")
            i += 1

        # Solicitar al usuario que seleccione una opción
        try:
            opcion = int(input(f"\nPor favor, seleccione una opción (1-{opcion_salir}): "))
        except:
            print(f"\nDebe ingresar un número entre 1 y {opcion_salir}.")

        # Mostrar la opción seleccionada

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            buscar_producto()
        elif opcion == 3:
            modificar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            consultar_inventario()
        elif opcion == opcion_salir:
            print("\n\t¡Gracias por utlizar nuestro sistema!\n\n\t¡Hasta pronto!\n")
        else:
            print(f"Debe ingresar un número entre 1 y {opcion_salir} inclusive.")
            continue
