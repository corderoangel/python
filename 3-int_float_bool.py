""" 
Enteros (int)
En Python, los enteros (int) son números sin parte decimal, como -5, 0, 42, etc.

Características:
Los enteros en Python pueden ser positivos o negativos.
No hay un límite en el tamaño de los enteros, ya que Python maneja la memoria de forma dinámica. 
"""

a = 10
b = 3

# Suma
suma = a + b  # Resultado: 13

# Resta
resta = a - b  # Resultado: 7

# Multiplicación
multiplicacion = a * b  # Resultado: 30

# División
division = a / b  # Resultado: 3.3333 (resultado flotante)

# División entera
division_entera = a // b  # Resultado: 3

# Módulo (residuo)
modulo = a % b  # Resultado: 1

# Potencia
potencia = a ** b  # Resultado: 1000 (10 elevado a 3)

# Métodos útiles para enteros:
"""
Aunque no hay muchos métodos específicos para enteros, hay algunas funciones incorporadas de Python 
que se usan con frecuencia:
"""
#abs(x): Devuelve el valor absoluto de un número.
abs(-5)  # Resultado: 5

#pow(x, y): Devuelve el valor de x elevado a la potencia y (similar a x ** y).
pow(2, 3)  # Resultado: 8

#divmod(x, y): Devuelve una tupla con la división entera y el residuo.
divmod(10, 3)  # Resultado: (3, 1)

#int(x): Convierte un número o cadena a un entero.
int("42")  # Resultado: 42
int(3.7)  # Resultado: 3 (trunca el decimal)

############################################################################################################
############################################################################################################
"""
Flotantes (float)
Los flotantes (float) son números que tienen parte decimal, como 3.14, -2.5 o 0.0.

Características:
Los flotantes en Python representan números reales con precisión limitada.
Pueden ser positivos o negativos.
Operaciones comunes con flotantes:
Las operaciones con números flotantes son similares a las de los enteros, pero los resultados 
siempre tienen parte decimal:
"""
a = 7.5
b = 2.0

# Suma
suma = a + b  # Resultado: 9.5

# Resta
resta = a - b  # Resultado: 5.5

# Multiplicación
multiplicacion = a * b  # Resultado: 15.0

# División
division = a / b  # Resultado: 3.75

# Potencia
potencia = a ** b  # Resultado: 56.25

#Métodos útiles para flotantes:
#round(x, n): Redondea un número flotante a n dígitos decimales.
round(3.14159, 2)  # Resultado: 3.14
"""float(x): Convierte un número o cadena a un flotante."""

float("3.14")  # Resultado: 3.14
float(5)  # Resultado: 5.0


#abs(x): Funciona de la misma forma que para enteros, devuelve el valor absoluto de un número flotante.
abs(-7.5)  # Resultado: 7.5

#Ejemplo práctico:
a = 5.5
b = 2.2

resultado = a + b
print(f"La suma de {a} y {b} es: {round(resultado, 2)}")  # Resultado: 7.7


############################################################################################################
############################################################################################################

#Booleanos (bool)
"""Los booleanos (bool) son un tipo de dato que solo puede tener dos valores: True (verdadero) 
o False (falso). Se utilizan principalmente en condiciones y estructuras de control.

Características:
Los booleanos se derivan de los números enteros: True es equivalente a 1 y False es equivalente a 0.
Se obtienen generalmente como resultado de comparaciones o evaluaciones lógicas.
Operaciones comunes con booleanos:
Operadores de comparación:

==: Igualdad
!=: Desigualdad
>: Mayor que
<: Menor que
>=: Mayor o igual que
<=: Menor o igual que
"""
a = 10
b = 5

resultado = a > b  # Resultado: True


"""
Operadores lógicos:

and: Devuelve True si ambas condiciones son verdaderas.
or: Devuelve True si al menos una condición es verdadera.
not: Invierte el valor de un booleano.
"""
a = True
b = False

print(a and b)  # Resultado: False
print(a or b)   # Resultado: True
print(not a)    # Resultado: False


"""Métodos útiles para booleanos:
Aunque no hay métodos específicos para los booleanos, puedes convertir otros tipos de datos a 
booleanos usando la función:
"""

#bool(x): Convierte un valor a booleano. Los valores "falsos" son 0, None, False, '' (cadena vacía), 
#listas o diccionarios vacíos. Cualquier otro valor se considera True.

bool(0)  # Resultado: False
bool(1)  # Resultado: True
bool("")  # Resultado: False
bool("Hola")  # Resultado: True

#Ejemplo práctico:
edad = 20
es_mayor_de_edad = edad >= 18

if es_mayor_de_edad:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")
