"""
Clase 4 - Ejercicio 2

Consumo de combustible

Realizar una aplicación en Python que a partir de la cantidad de litros de combustible que consume un coche por cada 100 km de recorrido, el costo de cada litro de combustible y la longitud del viaje realizado (en kilómetros), muestra un detalle de los litros consumidos y el dinero gastado.  

"""

# Constantes

consumo_km_litro = 12.0
precio_litro = 1048.0

print(" ")

# Entrada

recorrido = float(input("Ingrese los kilómetros recorridos: "))

print(" ")

# Procesamiento

litros_consumidos = recorrido / consumo_km_litro
costo_viaje = precio_litro * consumo_km_litro

# Salida

print(f"\tLitros consumidos: {litros_consumidos:.2f} litros.")

print(f"\tEl costo total del viaje es: ${costo_viaje:.2f}.")
