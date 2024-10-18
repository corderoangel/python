# Enteros (int)
"""
En Python, los enteros (int) son números sin parte decimal, como -5, 0, 42, etc.

Características:
- Los enteros en Python pueden ser positivos o negativos.
- No hay un límite en el tamaño de los enteros, ya que Python maneja la memoria de forma dinámica.
"""

# Declaración de variables enteras
a = 10
b = 3

# Suma de enteros
suma = a + b  # Resultado: 13

# Resta de enteros
resta = a - b  # Resultado: 7

# Multiplicación de enteros
multiplicacion = a * b  # Resultado: 30

# División de enteros (resultado flotante)
division = a / b  # Resultado: 3.3333

# División entera (trunca los decimales)
division_entera = a // b  # Resultado: 3

# Módulo (residuo de la división)
modulo = a % b  # Resultado: 1

# Potencia
potencia = a ** b  # Resultado: 1000 (10 elevado a 3)

# Funciones útiles para enteros:
"""
- abs(x): Devuelve el valor absoluto de un número.
- pow(x, y): Devuelve el valor de x elevado a la potencia y (similar a x ** y).
- divmod(x, y): Devuelve una tupla con la división entera y el residuo.
- int(x): Convierte un número o cadena a un entero.
"""

# Ejemplos:
abs(-5)  # Resultado: 5
pow(2, 3)  # Resultado: 8
divmod(10, 3)  # Resultado: (3, 1)
int("42")  # Resultado: 42
int(3.7)  # Resultado: 3 (trunca la parte decimal)


############################################################################################################

# Flotantes (float)
"""
Los flotantes (float) son números que tienen parte decimal, como 3.14, -2.5 o 0.0.

Características:
- Los flotantes representan números reales con precisión limitada.
- Pueden ser positivos o negativos.
- Las operaciones con números flotantes son similares a las de los enteros, pero los resultados
  siempre tienen parte decimal.
"""

# Declaración de variables flotantes
a = 7.5
b = 2.0

# Suma de flotantes
suma = a + b  # Resultado: 9.5

# Resta de flotantes
resta = a - b  # Resultado: 5.5

# Multiplicación de flotantes
multiplicacion = a * b  # Resultado: 15.0

# División de flotantes
division = a / b  # Resultado: 3.75

# Potencia con flotantes
potencia = a ** b  # Resultado: 56.25

# Funciones útiles para flotantes:
"""
- round(x, n): Redondea un número flotante a n dígitos decimales.
- float(x): Convierte un número o cadena a un flotante.
- abs(x): Funciona de la misma forma que para enteros, devuelve el valor absoluto de un número flotante.
"""

# Ejemplos:
round(3.14159, 2)  # Resultado: 3.14
float("3.14")  # Resultado: 3.14
float(5)  # Resultado: 5.0
abs(-7.5)  # Resultado: 7.5

# Ejemplo práctico:
a = 5.5
b = 2.2
resultado = a + b
print(f"La suma de {a} y {b} es: {round(resultado, 2)}")  # Resultado: 7.7


############################################################################################################

# Booleanos (bool)
"""
Los booleanos (bool) son un tipo de dato que solo puede tener dos valores: True (verdadero) o False (falso).
Se utilizan principalmente en condiciones y estructuras de control.

Características:
- Los booleanos derivan de los enteros: True es equivalente a 1 y False es equivalente a 0.
- Se obtienen como resultado de comparaciones o evaluaciones lógicas.
"""

# Operaciones comunes con booleanos (comparaciones):
a = 10
b = 5

# Comparación: mayor que
resultado = a > b  # Resultado: True

# Operadores lógicos:
"""
- and: Devuelve True si ambas condiciones son verdaderas.
- or: Devuelve True si al menos una condición es verdadera.
- not: Invierte el valor de un booleano.
"""

a = True
b = False

print(a and b)  # Resultado: False
print(a or b)   # Resultado: True
print(not a)    # Resultado: False

# Funciones útiles para booleanos:
"""
- bool(x): Convierte un valor a booleano. Los valores "falsos" incluyen 0, None, False, '' (cadena vacía),
  listas o diccionarios vacíos. Cualquier otro valor se considera True.
"""

# Ejemplos:
bool(0)  # Resultado: False
bool(1)  # Resultado: True
bool("")  # Resultado: False
bool("Hola")  # Resultado: True

# Ejemplo práctico con condicional:
edad = 20
es_mayor_de_edad = edad >= 18

if es_mayor_de_edad:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")
