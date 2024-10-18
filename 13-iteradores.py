# Ejemplo de uso de iteradores en Python

# 1. Ejemplo básico de iterador
# Crear una lista de números
my_list = [1, 2, 3, 4]

# Obtener el iterador de la lista
my_iter = iter(my_list)

# Usar el iterador para imprimir cada elemento de la lista
print(next(my_iter))  # Imprime el primer elemento: 1
print(next(my_iter))  # Imprime el segundo elemento: 2
print(next(my_iter))  # Imprime el tercer elemento: 3
print(next(my_iter))  # Imprime el cuarto elemento: 4
# La siguiente línea descomentada causaría un error StopIteration si se ejecuta, ya que no hay más elementos.
# print(next(my_iter))  # Descomentar causará error

# 2. Crear un iterador para los números impares
# Definir el límite hasta donde se generarán números impares
limit = 10

# Crear un iterador que genere números impares en el rango especificado
odd_iter = iter(range(1, limit + 1, 2))  # range(1, 11, 2) genera 1, 3, 5, 7, 9

# Usar el iterador para imprimir cada número impar
for num in odd_iter:
    print(num)  # Imprime cada número impar: 1, 3, 5, 7, 9

# 3. Iterar sobre una cadena
# Crear una cadena de texto
text = "Hola mundo"

# Crear un iterador para la cadena
iter_text = iter(text)

# Usar el iterador para imprimir cada carácter en la cadena
for char in iter_text:
    print(char)  # Imprime cada carácter en la cadena: H, o, l, a,  , m, u, n, d, o
