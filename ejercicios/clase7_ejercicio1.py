"""
Clase 7 - Ejercicio 1

Registro de productos en un inventario

Vas a implementar un sistema básico para registrar productos en el inventario de una tienda. El programa debe permitir que el usuario agregue productos a una lista hasta que decida no agregar más. Luego, deberás mostrar todos los productos ingresados al inventario.
"""

titulo_registro = "Alta de productos"
titulo_codigo = "Código"
titulo_nombre = "Nombre del producto"
titulo_precio = "Precio" + " " * 10
titulo_cantidad = "Cantidad en stock"
titulo_lista = "Lista de productos"

lista_productos = []

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

    continuar = (
        input("¿Desea agregar otro producto? Ingrese 's' o 'n': ").lower() == "s"
    )

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
