#Paso 2. Condicionales y Bucles
#Crear un script que pida al usuario un número y determine si es par o impar
#utilizando condicionales (if, else).

numero = int(input("Escribe un número: "))

if numero % 2 == 0:
    print("Es un número par")
else:
    print("Es un número impar")

#Implementar un bucle for para iterar sobre una lista de números e imprimir sus
# cuadrados
numeros = [1, 2, 3, 4, 5]

for n in numeros:
    print("El cuadrado de", n, "es", n**2)

# Usar un bucle while para solicitar repetidamente la entrada del usuario hasta que
# se cumpla una condición específica.

respuesta = ""

while respuesta != "si":
    respuesta = input("¿Ya estudiaste? (escribe 'si' para salir): ")

print("¡Muy bien!")


