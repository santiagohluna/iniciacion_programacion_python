"""
Proyecto final

"""

import os

# Menú de opciones

opciones = {
    1: "Alta de productos nuevos",
    2: "Consulta de datos de productos",
    3: "Modificar la cantidad en stock de un producto",
    4: "Dar de baja productos",
    5: "Listado completo de productos",
    6: "Salir",
}

# Inicialzación de variables.

opcion = 0

opcion_salir = int(list(opciones.keys())[list(opciones.values()).index("Salir")])

titulo_menu_ppal = "Menú de gestión de productos."
titulo_registro = "Alta de productos"
titulo_codigo = "Código"
titulo_nombre = "Nombre del producto"
titulo_precio = "Precio" + " " * 10
titulo_cantidad = "Cantidad en stock"
titulo_lista = "Lista de productos"

lista_productos = []

# Definición de funciones.


# Limpiar pantalla
def limpiar_pantalla():
    os.system("clear")


def agregar_producto():
    limpiar_pantalla()
    print(" ")
    print(titulo_registro)
    print("=" * len(titulo_registro))
    print(" ")
    continuar = True
    while continuar:
        codigo = int(input("Ingrese el código del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad en stock: "))

        lista_productos.append([codigo, nombre, precio, cantidad])

        print(" ")
        continuar = (
            input("¿Desea agregar otro producto? Ingrese 's' o 'n': ").lower() == "s"
        )
        print(" ")


def consultar_producto():
    limpiar_pantalla()
    continuar = True
    while continuar:
        print("Funcionalidad no implementada aún")
        continuar = (
            input("Pulse una tecla para volver al menú principal: ").lower() == " "
        )


def modificar_producto():
    limpiar_pantalla()
    continuar = True
    while continuar:
        print("Funcionalidad no implementada aún")
        continuar = (
            input("Pulse una tecla para volver al menú principal: ").lower() == " "
        )


def eliminar_producto():
    limpiar_pantalla()
    continuar = True
    while continuar:
        print("Funcionalidad no implementada aún")
        continuar = (
            input("Pulse una tecla para volver al menú principal: ").lower() == " "
        )


def consultar_inventario():
    limpiar_pantalla()
    continuar = True
    while continuar:
        print(" ")
        print(titulo_lista)
        print("=" * len(titulo_lista))
        print(" ")
        print(f"{titulo_codigo} {titulo_nombre} {titulo_precio} {titulo_cantidad}")
        print(
            "=" * len(titulo_codigo)
            + " "
            + "=" * len(titulo_nombre)
            + " "
            + "=" * len(titulo_precio)
            + " "
            + "=" * len(titulo_cantidad)
        )
        indice = 0
        while indice < len(lista_productos):
            codigo = lista_productos[indice][0]
            nombre = lista_productos[indice][1]
            precio = lista_productos[indice][2]
            cantidad = lista_productos[indice][3]
            print(
                f"{codigo}"
                + " " * (len(titulo_codigo) - len(str(codigo)))
                + " "
                + f"{nombre}"
                + " " * (len(titulo_nombre) - len(nombre))
                + " "
                + f"{precio}"
                + " " * (len(titulo_precio) - len(str(precio)))
                + " "
                + f"{cantidad}"
            )
            indice += 1

        continuar = (
            input("¿Desea volver al menú principal? Ingrese 's' o 'n': ").lower() == "n"
        )


# Programa principal.

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

    print()
    opcion = int(input(f"Por favor, seleccione una opción (1-{opcion_salir}): "))

    # Mostrar la opción seleccionada

    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        consultar_producto()
    elif opcion == 3:
        modificar_producto()
    elif opcion == 4:
        eliminar_producto()
    elif opcion == 5:
        consultar_inventario()
    elif opcion == opcion_salir:
        print("\n\t¡Hasta pronto!\n")
    else:
        print(f"Debe ingresar un número entre 1 y {opcion_salir} inclusive.")
        continue
