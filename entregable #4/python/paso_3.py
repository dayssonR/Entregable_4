# Paso 3. Listas y Diccionarios
# - Crear una lista de elementos, como nombres de estudiantes, y mostrar cada uno
# utilizando un bucle.
estudiantes = ["Ana", "Luis", "Pedro", "María"]

for nombre in estudiantes:
    print("Estudiante:", nombre)

# Crear un diccionario simple que almacene información de contacto (nombre,
# correo) y mostrar sus claves y valores.
contacto = {
    "nombre": "Carlos",
    "correo": "carlos@email.com"
}

print("Nombre:", contacto["nombre"])
print("Correo:", contacto["correo"])

# Implementar un script que permita al usuario agregar elementos a una lista o
# actualizar valores en un diccionario.

# Lista
frutas = []
nueva_fruta = input("Escribe una fruta para agregar a la lista: ")
frutas.append(nueva_fruta)
print("Lista de frutas:", frutas)

# Diccionario
persona = {"nombre": "Laura", "edad": 20}
nueva_edad = int(input("Escribe la nueva edad de Laura: "))
persona["edad"] = nueva_edad
print("Datos actualizados:", persona)

