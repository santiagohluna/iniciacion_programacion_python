"""
Clase 6 - Ejercicio 1

Control de stock de productos

Desarrollá un programa que permita al usuario ingresar el nombre de varios productos y la cantidad en stock que hay de cada uno. El programa debe seguir pidiendo que ingrese productos hasta que el usuario decida salir, ingresando "salir" como nombre de producto. Después de que el bucle termine, el programa debe mostrar la cantidad total de productos ingresados.

"""

menu = "Menú de opciones"
titulo_productos = "Nombre del producto"
titulo_stock = "Cantidad en stock"

productos = {}
data_producto = []


def mostrar_productos():
    print("Mostrando los productos:")
    print(" ")
    print("=" * 2 + "\t" + "=" * len(titulo_productos) + "\t" + "=" * len(titulo_stock))
    print(f"id\t{titulo_productos}\t{titulo_stock}")
    print("=" * 2 + "\t" + "=" * len(titulo_productos) + "\t" + "=" * len(titulo_stock))
    for id in productos:
        print(
            f"{productos[id][0]}"
            + f"\t{productos[id][1]}"
            + " " * (len(titulo_productos) - len(productos[id][1]))
            + f"\t{productos[id][2]}"
        )


def agregar_producto():
    i = 0
    ingresar = "s"
    while ingresar == "s":
        producto = input("Ingrese el nombre del producto: ")
        stock = int(input("Ingrese el stock del producto: "))
        id = i + 1
        productos[i] = [id, producto, stock]
        i += 1
        print(" ")
        print("Producto agregado exitosamente.")
        print(" ")
        ingresar = input(
            "¿Desea agregar otro producto? Ingrese 's' para agregar o 'n' para volver al menú principal: "
        ).lower()
        print(" ")


# Entrada

opcion = 0

while opcion != 3:
    print(" ")
    print("=" * len(menu))
    print(menu)
    print("=" * len(menu))
    print(" ")
    print("\t1. Ver productos.")
    print("\t2. Agregar producto y stock.")
    print("\t3. Salir.")
    print(" ")

    opcion = int(input("Seleccione una opción: "))
    print(" ")

    if opcion == 1:
        mostrar_productos()
    elif opcion == 2:
        agregar_producto()
    elif opcion == 3:
        print("¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")

# Procesamiento


# Salida
