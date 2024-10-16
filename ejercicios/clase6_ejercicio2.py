"""
Clase 6 - Ejercicio 2

Validación de precios de productos

Escribí un programa que permita al usuario ingresar el precio de un producto, pero que sólo acepte valores mayores a 0.

Si el usuario ingresa un valor inválido (negativo o cero), el programa debe mostrar un mensaje de error, y volver a pedir el valor hasta que se ingrese uno válido. Al final, el programa debe mostrar el precio aceptado.
"""

condicion = True

while condicion:
    precio = float(input("Ingrese el precio del producto: "))
    condicion = precio <= 0
    if condicion:
        print("El precio debe ser mayor a $0.00")

print(f"El precio ingresado es: ${precio:.2f}.")
