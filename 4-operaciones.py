# Declaración de variables
a = 10
b = 10

# Suma
print("Suma:", a + b)  # Resultado: 20

# Resta
print("Resta:", a - b)  # Resultado: 0

# Multiplicación
print("Multiplicación:", a * b)  # Resultado: 100

# Potenciación
print("Potenciación:", a ** b)  # Resultado: 10000000000 (10 elevado a la 10)

# División
print("División:", a / b)  # Resultado: 1.0 (resultado flotante)

# División entera
print("Parte entera de la división:", a // b)  # Resultado: 1 (resultado entero)

# Módulo (residuo)
print("Módulo:", a % b)  # Resultado: 0 (residuo de la división de 10 entre 10)

a /= 2
print(a)  # Resultado: 5.0 (a ahora es un número flotante)

# Operación sin paréntesis, sigue la precedencia de operadores (multiplicación antes que suma)
operation_1  = 2 + 3 * 4
print(operation_1)  # Resultado: 14 (primero se multiplica 3 * 4 y luego se suma 2)

# Operación con paréntesis, altera la precedencia
operation_2  = (2 + 3) * 4
print(operation_2)  # Resultado: 20 (primero se suma 2 + 3 y luego se multiplica por 4)

# Operación compleja con diferentes operadores y precedencias
operation_3 = (2+3) * (4**2) / 8 - 1
print(operation_3)  # Resultado: 11.0


# Redefinición de las variables
a = 10
b = 3

# Comparaciones
print(a > b)   # Resultado: True (10 es mayor que 3)
print(a < b)   # Resultado: False (10 no es menor que 3)
print(a >= b)  # Resultado: True (10 es mayor o igual que 3)
print(a <= b)  # Resultado: False (10 no es menor o igual que 3)
print(a == b)  # Resultado: False (10 no es igual a 3)
print(a != b)  # Resultado: True (10 es diferente de 3)
