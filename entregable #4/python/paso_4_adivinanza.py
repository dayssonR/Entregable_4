# Crear un juego de adivinanza donde el programa genere un número aleatorio y el
# usuario deba adivinarlo, recibiendo pistas de "mayor" o "menor" en cada intento.

import random

numero_secreto = random.randint(1, 10)
adivina = 0

print("Adivina el número entre 1 y 10")

while adivina != numero_secreto:
    adivina = int(input("Tu número: "))

    if adivina < numero_secreto:
        print("Es más grande")
    elif adivina > numero_secreto:
        print("Es más pequeño")

print("¡Felicidades! Adivinaste el número.")
