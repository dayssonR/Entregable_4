# Script de Resolución de Problemas Simples
# - Desarrollar un programa que simule una calculadora básica, permitiendo al usuario
# realizar sumas, restas, multiplicaciones y divisiones.

print("Calculadora")
num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))

print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir")
opcion = input("Elige una opción (1-4): ")

if opcion == "1":
    print("Resultado:", num1 + num2)
elif opcion == "2":
    print("Resultado:", num1 - num2)
elif opcion == "3":
    print("Resultado:", num1 * num2)
elif opcion == "4":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("No se puede dividir por cero")
else:
    print("Opción no válida")

