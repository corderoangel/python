# Definición de funciones lambda para operaciones matemáticas

# Sumar dos números
add = lambda a, b: a + b
# Imprimir el resultado de la suma de 10 y 4
print(add(10, 4))

# Multiplicar dos números
multiply = lambda a, b: a * b
# Imprimir el resultado de la multiplicación de 80 y 5
print(multiply(80, 5))

# Cuadrado de cada número en un rango
numbers = range(11)  # Rango de números del 0 al 10

# Usar map para aplicar la función lambda que calcula el cuadrado a cada número en el rango
squared_numbers = list(map(lambda x: x**2, numbers))
# Imprimir la lista de cuadrados
print("Cuadrados:", squared_numbers)

# Filtrar los números pares
# Usar filter para aplicar la función lambda que verifica si un número es par
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# Imprimir la lista de números pares
print("Pares:", even_numbers)
