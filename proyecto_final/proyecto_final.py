"""
Proyecto final

"""

# Menú de opciones

opciones = {
    1: "Alta de productos nuevos",
    2: "Consulta de datos de productos",
    3: "Modificar la cantidad en stock de un producto",
    4: "Dar de baja productos",
    5: "Listado completo de productos",
    6: "Lista de productos con cantidad bajo mínimo",
    7: "Salir",
}

opcion = 0

while opcion != 7:
    i = 1
    print()
    print("Menú de gestión de productos.\n")
    for opt in opciones:
        print(f"{i}. {opciones[i]}.")
        i += 1

    # Solicitar al usuario que seleccione una opción

    print()
    opcion = int(input("Por favor, seleccione una opción (1-7): "))

    # Mostrar la opción seleccionada

    if opcion >= 1 and opcion <= 7:
        print(f"Ha seleccionado la opción {opcion}: {opciones[opcion]}.")
    else:
        print("Debe ingresar un número entre 1 y 7 inclusive.")
        continue
