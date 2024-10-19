# Ejemplo de uso de bucles: for y while

# Definición de una lista de números
numbers = [1, 2, 3, 4, 5, 6]

# Bucle for que itera sobre la lista de números
for i in numbers:
    print("Aquí i es igual a:", i + 1)  # Imprime el valor de i incrementado en 1

# Bucle for que itera sobre un rango de números del 3 al 9 (excluyendo 10)
for i in range(3, 10):
    print(i)  # Imprime cada número en el rango

# Definición de una lista de frutas
fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]

# Bucle for que itera sobre la lista de frutas
for fruit in fruits:
    print(fruit)  # Imprime el nombre de la fruta
    # Condición para buscar la fruta "Naranja"
    if fruit == "Naranja":
        print("Naranja encontrada")  # Mensaje si se encuentra la fruta

# Inicialización de la variable x
x = 0
# Bucle while que continúa mientras x sea menor que 5
while x < 5:
    # Condición para salir del bucle si x es igual a 3
    if x == 3:
        break  # Termina el bucle
    print(x)  # Imprime el valor de x
    x += 1  # Incrementa x en 1

# Reutilización de la lista de números
numbers = [1, 2, 3, 4, 5, 6]
# Bucle for que itera sobre la lista de números
for i in numbers:
    # Condición para salir del bucle si i es igual a 3
    if i == 3:
        break  # Termina el bucle
    print("Aquí i es igual a:", i)  # Imprime el valor de i
