""" 
Clase 2 - Ejercicio 2

Ingreso promedio.

Consigna: Escribir un programa que guarde en variables el monto del ingreso de cada uno de los primeros 6 meses del año.

Luego, calcular y guardar en otra variable el promedio de esos valores.

Por último, mostrar una leyenda que diga “El ingreso promedio en el semestre es de xxxxx” donde “xxxxx” es el valor calculado.

"""

ingresos = [1000.0, 1100.0, 1120.0, 1230.0, 1320.0, 1350.0]

suma_ingresos = 0.0

for ingreso in ingresos:
    suma_ingresos += ingreso

ingreso_promedio = suma_ingresos / len(ingresos)

print(f"El ingreso promedio en el semestre es de ${ingreso_promedio:.2f}")
