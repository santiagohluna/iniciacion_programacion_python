"""
Clase 03 - Ejercicio 02

Calculadora de propinas
Escribe un programa en Python que calcule la propina que se debe dejar en un restaurante.

El script debe solicitar al usuario el monto total de la cuenta y el porcentaje de propina que desea dejar.
 
Utilizando operadores aritméticos, calcula la cantidad de propina y el total a pagar (incluyendo la propina).
Finalmente, muestra los resultados en la pantalla.
"""

# Entrada

monto_total = float(input("Ingrese el monto total de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))

# Procesamiento

propina = monto_total * porcentaje_propina / 100.0
total_con_propina = monto_total + propina

# Salida

print(f"\tLa propina a dejar es: ${propina:.2f}.")
print(f"\tEl total con la propina incluida es: ${total_con_propina:.2f}.")
