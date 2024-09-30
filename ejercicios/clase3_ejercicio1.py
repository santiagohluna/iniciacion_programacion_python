"""

Clase 03 - Ejercicio 01

Operaciones básicas

Crea un programa que solicite al usuario dos números enteros.

Realiza las siguientes operaciones: suma, resta, multiplicación, y módulo.

Muestra el resultado de cada operación en un formato claro y amigable.

Asegúrate de incluir mensajes personalizados que expliquen cada resultado, por ejemplo: "La suma de tus números es: X".

"""

operaciones = {1: "Suma", 2: "Resta", 3: "Multiplicación", 4: "Resto"}

# Entrada

numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese otro numero: "))

print("Seleccione la operación a realizar:")
print("\t 1. Sumar.")
print("\t 2. Restar.")
print("\t 3. Multiplicar.")
print("\t 4. Resto.")

opcion = int(input("Ingrese el numero correspondiente a la opción deseada: "))
print(f"Usted eligió la opción {opcion}.")

# Procesamiento

if opcion == 1:
    resultado = numero_1 + numero_2
elif opcion == 2:
    resultado = numero_1 - numero_2
elif opcion == 3:
    resultado = numero_1 * numero_2
elif opcion == 4:
    resultado = numero_1 % numero_2
else:
    print("Error en el identificador de la opción.")

# Salida

print(f"El resultado de la operación {operaciones[opcion]} es {resultado}")
