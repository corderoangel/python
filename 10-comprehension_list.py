# Generación de listas mediante comprensiones y transposición de matrices

# 1. Generación de cuadrados de números del 1 al 10
squares = [x**2 for x in range(1, 11)]
# print("Cuadrados:", squares)  # Imprimir la lista de cuadrados (comentado para no mostrar)

# 2. Conversión de temperaturas de Celsius a Fahrenheit
celsius = [0, 10, 20, 30, 40]
# La fórmula de conversión es incorrecta. La fórmula correcta es: (temp * 9/5) + 32
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
# print("Temperatura en F:", fahrenheit)  # Imprimir la lista de temperaturas en Fahrenheit (comentado para no mostrar)

# 3. Filtración de números pares entre 1 y 20
evens = [x for x in range(1, 21) if x % 2 == 0]
# print(evens)  # Imprimir la lista de números pares (comentado para no mostrar)

# 4. Definición de una matriz
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 5. Transposición de la matriz utilizando comprensión de listas
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)  # Imprimir la matriz original
# print(transposed)  # Imprimir la matriz transpuesta (comentado para no mostrar)

# 6. Transposición de la matriz utilizando bucles tradicionales
transposed = []
for i in range(len(matrix[0])):
    transposed_row = []  # Inicializar una nueva fila para la matriz transpuesta
    for row in matrix:
        transposed_row.append(row[i])  # Añadir el elemento correspondiente de cada fila
    transposed.append(transposed_row)  # Añadir la fila transpuesta a la matriz transpuesta

print(transposed)  # Imprimir la matriz transpuesta
