numbers = {1: "uno", 2: "dos", 3: "tres"}  # Diccionario de números
print(numbers[2])  # Imprime: "dos" (Valor asociado a la clave 2)

information = {
    "nombre": "Carla",
    "Apellido": "Florida",
    "Altura": 1.60,
    "Edad": 29
}
print(information)  # Imprime todo el diccionario

del information["Edad"]  # Elimina el par clave-valor con la clave "Edad"
print(information)  # Imprime el diccionario sin la clave "Edad"

claves = information.keys()  # Obtiene todas las claves del diccionario
print(claves)  # Imprime: dict_keys(['nombre', 'Apellido', 'Altura'])

values = information.values()  # Obtiene todos los valores del diccionario
print(values)  # Imprime: dict_values(['Carla', 'Florida', 1.6])

pairs = information.items()  # Obtiene todos los pares clave-valor
print(pairs)  # Imprime: dict_items([('nombre', 'Carla'), ('Apellido', 'Florida'), ('Altura', 1.6)])

contacts = {
    "Carla": {"Apellido": "Florida", "Altura": 1.60, "Edad": 29},
    "Diego": {"Apellido": "Antezana", "Altura": 1.80, "Edad": 32}
}
print(contacts["Carla"])  # Imprime la información de "Carla"
