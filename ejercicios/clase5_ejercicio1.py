"""
Clase 05 - Ejercicio 1

Control de inventario de una tienda de videojuegos

Imaginá que estás ayudando a una tienda de videojuegos a organizar su inventario. El dueño te pide que escribas un programa que verifique si hay stock suficiente de un videojuego y, si no hay, que avise que hay que reponerlo. 


El programa debería pedirle al usuario que ingrese la cantidad actual en stock y, en base a esa cantidad, mostrar si se necesita hacer un nuevo pedido o no.
"""

cantidad_minima = 5

cantidad_stock = int(input("Ingrese la cantidad actual en stock del producto: "))

if cantidad_stock <= cantidad_minima:
    print("Se debe hacer un nuevo pedido del producto.")
else:
    print("La cantidad en stock es suficiente.")
