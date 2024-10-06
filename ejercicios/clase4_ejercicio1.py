"""
Clase 4 - Ejercicio 1

Ticket de la compra

Consigna:

    - Escribir un programa que solicite el nombre, la cantidad y el valor unitario de tres productos.
    - Luego, debe calcular el importe de IVA (21%) de cada producto.
    - Por último, debe mostrar en la terminal el ticket de la operación con todos los datos de la compra. 

"""

import pandas as pd

nombres = []
precios = []
cantidades = []

# Entrada

for i in [1, 2, 3]:
    print(" ")
    print(f"Producto {i}:")
    nombre_producto = input("\tIngrese el nombre del producto: ")
    nombres.append(nombre_producto)
    precio = float(input("\tIngrese el precio: "))
    precios.append(precio)
    cantidad = int(input("\tIngrese la cantidad: "))
    cantidades.append(cantidad)

# nombres = ["Leche", "Azúcar", "Yerba"]
# precios = [1190.0, 1200.0, 3500.0]
# cantidades = [4, 2, 3]
precio_con_IVA = []

productos = {"Nombre": nombres, "Precio": precios, "Cantidad": cantidades}

# Procesamiento

df = pd.DataFrame(productos)

df["Importe IVA"] = df["Precio"] * 0.21

df["Precio con IVA"] = df["Precio"] * 1.21

df["Subtotal"] = df["Precio con IVA"] * df["Cantidad"]

# Salida

print(" ")
print("======")
print("Ticket")
print("======")
print(" ")
print(df)
print(" ")
print(f"Total: ${df['Subtotal'].sum():.2f}")
