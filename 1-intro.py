"""
Archivo: variables.py
Descripción: Este archivo contiene una introducción a las variables en Python,
incluyendo su declaración, tipos, buenas prácticas, asignación múltiple, intercambio
de valores, tipos mutables e inmutables, conversión de tipos y ejemplos prácticos.
"""

# ------------------------------
# Declaración de Variables
# ------------------------------
# Las variables en Python no requieren una declaración explícita de tipo.
# Se crean y se les asigna valor con el operador `=`.

nombre = "Ángel"         # String: Cadena de texto
edad = 23                # int: Número entero
altura = 1.72            # float: Número decimal
es_programador = True     # bool: Valor booleano (Verdadero/Falso)

# ------------------------------
# Tipos de Variables
# ------------------------------
# Las variables en Python pueden tener diferentes tipos de datos. A continuación, algunos ejemplos.

edad = 30                # int: Entero
precio = 12.99           # float: Decimal (flotante)
nombre = "Ángel"         # string: Texto
es_adulto = True         # bool: Booleano (True o False)
lista_numeros = [1, 2, 3, 4, 5]  # list: Lista (colección ordenada de elementos)
persona = {"nombre": "Ángel", "edad": 23}  # dict: Diccionario (pares clave-valor)
nada = None              # NoneType: Representa la ausencia de valor o vacío

# ------------------------------
# Buenas Prácticas para Nombres de Variables
# ------------------------------
# 1. El nombre de una variable debe empezar con una letra o un guion bajo (_), pero no con un número.
# 2. Los nombres de variables solo pueden contener letras, números y guiones bajos (_).
# 3. Python distingue entre mayúsculas y minúsculas (por ejemplo, 'nombre' y 'Nombre' son variables diferentes).
# 4. Es recomendable usar nombres descriptivos y significativos para las variables,
#    para que tu código sea fácil de entender y mantener.

# Ejemplos de nombres adecuados:
nombre_completo = "Ángel López"
total_precio = 150.75
es_valido = False

# ------------------------------
# Asignación Múltiple
# ------------------------------
# Python permite asignar varios valores a varias variables en una sola línea.
a, b, c = 10, 20, 30

# ------------------------------
# Intercambio de Valores en Variables
# ------------------------------
# Una técnica común en Python es intercambiar valores entre variables de manera directa.
a, b = b, c  # Ahora, a toma el valor de b y b toma el valor de c

# ------------------------------
# Tipos de Variables Mutables e Inmutables
# ------------------------------
# **Inmutables**: Su contenido no se puede cambiar después de haber sido creado. Ejemplos: `int`, `float`, `str`, `tuple`.
# **Mutables**: Su contenido puede cambiar después de haber sido creado. Ejemplos: `list`, `dict`, `set`.

# Ejemplos de tipos inmutables:
numero_entero = 100       # int (inmutable)
texto = "Hola, mundo"     # str (inmutable)
tupla = (1, 2, 3)         # tuple (inmutable)

# Ejemplos de tipos mutables:
lista = [1, 2, 3, 4, 5]   # list (mutable)
diccionario = {"nombre": "Ángel", "edad": 23}  # dict (mutable)
conjunto = {1, 2, 3}      # set (mutable)

# ------------------------------
# Conversión de Tipos
# ------------------------------
# En Python, es posible convertir variables de un tipo a otro utilizando funciones de conversión.

edad = 23
edad_str = str(edad)  # Convierte el entero 23 en el string "23"

numero = "123"
numero_int = int(numero)  # Convierte el string "123" en el entero 123

altura = 1.72
altura_entero = int(altura)  # Convierte el flotante 1.72 en el entero 1 (truncando el decimal)

# ------------------------------
# Ejemplos Prácticos
# ------------------------------
# A continuación, se presentan algunos ejemplos prácticos de cómo se pueden utilizar las variables en Python.

# Mostrar información usando f-strings (manera recomendada de formatear cadenas)
print(f"Nombre: {nombre}")  # Salida: Nombre: Ángel
print(f"Edad: {edad}")       # Salida: Edad: 23
print(f"Altura: {altura}")   # Salida: Altura: 1.72
print(f"¿Es programador?: {es_programador}")  # Salida: ¿Es programador?: True

# Realizar operaciones aritméticas con variables
print(f"Edad actualizada: {edad + 1}")  # Salida: Edad actualizada: 24

# ------------------------------
# Notas Adicionales
# ------------------------------
# 1. Evitar usar nombres de variables que puedan entrar en conflicto con palabras clave de Python (como `def`, `for`, `class`, etc.).
# 2. Mantén tu código limpio y organizado comentando adecuadamente y utilizando nombres descriptivos para tus variables.
# 3. Si trabajas con grandes bloques de código, agrupa tus variables por contexto o funcionalidad para mejorar la legibilidad.

