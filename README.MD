## Strings

Los strings son secuencias de caracteres, como palabras o frases. Se pueden definir usando comillas simples ('...') o comillas dobles ("...").

```python
# Ejemplo de strings
mi_string = "Hola, mundo"
print(mi_string)  # Salida: Hola, mundo
```

**Concatenación:** Combinar dos o más strings.

```python
saludo = "Hola" + " " + "mundo"
print(saludo)  # Salida: Hola mundo
```

**Repetición:** Repetir un string varias veces.

```python
repetido = "Hola" \* 3
print(repetido) # Salida: HolaHolaHola
```

**Acceso por índice:** Los strings son indexados, comenzando desde 0.

```python
Copiar código
letra = mi_string[0] # 'H'
```

## int, float, bool

Estos son los tipos de datos básicos en Python:

**int:** Números enteros.

```python
entero = 5
```

**float:** Números con decimales.

```python
decimal = 3.14
```

**bool:** Representa valores booleanos (True o False).

```python
Copiar código
verdadero = True
falso = False
```

## Operaciones

Python permite realizar operaciones matemáticas con operadores básicos.

**Suma:** +
**Resta:** -
**Multiplicación:** \*
**División:** /
**Módulo (resto de la división):** %
**Potencia:** \*\*

```python
x = 10
y = 3

suma = x + y       # 13
resta = x - y      # 7
multiplicacion = x * y  # 30
division = x / y   # 3.3333
modulo = x % y     # 1
potencia = x ** y  # 1000
```

## input

La función input() permite obtener datos del usuario en forma de string. Puedes convertir el valor a otros tipos de datos si es necesario.

```python
nombre = input("¿Cómo te llamas? ")
print("Hola, " + nombre)

edad = int(input("¿Cuántos años tienes? "))  # Convertir a entero
print("Tienes " + str(edad) + " años")
```

## Listas

Las listas son estructuras que permiten almacenar múltiples elementos. Se definen con corchetes ([]) y pueden contener diferentes tipos de datos.

```python
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista[0])  # Salida: 1
```

**Añadir elementos:** Usar el método `append()`.

```python
mi_lista.append(6)
```

**Eliminar elementos:** Usar `remove()` o `pop()`.

```python
mi_lista.remove(3) # Elimina el primer valor igual a 3
```

**Longitud de la lista:** Usar `len()`.

```python
print(len(mi_lista)) # Número de elementos en la lista
```

## Slice

El slice permite obtener subconjuntos de listas o strings mediante rangos de índices.

```python
mi_lista = [10, 20, 30, 40, 50]

# Slice desde el índice 1 al 3 (excluyendo el 4)

sub_lista = mi_lista[1:4] # [20, 30, 40]

# Slice omitiendo el primer o último índice

sub_lista = mi_lista[:3] # [10, 20, 30]
sub_lista = mi_lista[2:] # [30, 40, 50]
```

## Listas parte 2 (dimensiones y tuplas)

### Listas multidimensionales

Son listas dentro de listas, como matrices o tablas.

```python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[1][2]) # Salida: 6 (segunda fila, tercer elemento)
```

### Tuplas

Las tuplas son similares a las listas, pero son inmutables, lo que significa que no se pueden modificar después de ser creadas. Se definen usando paréntesis (()).

```python
mi_tupla = (1, 2, 3)
print(mi_tupla[0]) # Salida: 1
```

## Diccionarios

Los diccionarios en Python son colecciones desordenadas de elementos que contienen pares de clave-valor. Se definen con llaves {}.

```python
# Definir un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

# Acceder a un valor usando su clave
print(mi_diccionario["nombre"])  # Salida: Juan

# Añadir o modificar un valor
mi_diccionario["profesión"] = "Ingeniero"
```

### Métodos útiles:

**keys():** Devuelve todas las claves del diccionario.
**values():** Devuelve todos los valores.
**items():** Devuelve pares clave-valor.

```python
print(mi_diccionario.keys()) # Salida: dict_keys(['nombre', 'edad', 'ciudad', 'profesión'])
print(mi_diccionario.values()) # Salida: dict_values(['Juan', 25, 'Madrid', 'Ingeniero'])
```

## Comprehension List

Las comprehension lists permiten crear listas de forma concisa y eficiente en una sola línea, a partir de iteraciones y condiciones.

```python
# Sintaxis básica: [expresión for elemento in iterable]
cuadrados = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Con condiciones: [expresión for elemento in iterable if condición]
pares = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

También se puede usar en diccionarios o conjuntos:

```python
# Diccionario comprehension

cuadrados_dict = {x: x ** 2 for x in range(5)} # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Condicionales

Los condicionales permiten ejecutar código basado en condiciones específicas usando `if`, `elif (else if)` y `else`.

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres adolescente.")
else:
    print("Eres un niño.")
```

**Operadores de comparación:**
`==`: Igual a
`!=`: Diferente de

`>`: Mayor que
`> <`: Menor que
`> =`: Mayor o igual que
`> <=`: Menor o igual que
`>`: Operadores lógicos:

`and`: Ambas condiciones deben ser verdaderas.
`or`: Al menos una condición debe ser verdadera.
`not`: Invierte el valor lógico.

## Ciclos for y while

**For**
El ciclo for se usa para iterar sobre elementos en una secuencia (listas, strings, diccionarios, etc.).

```python
# Iterar sobre una lista
mi_lista = [1, 2, 3, 4, 5]
for numero in mi_lista:
    print(numero)
```

También se puede usar con la función range() para iterar un número específico de veces:

```python
for i in range(5):
print(i) # Salida: 0, 1, 2, 3, 4
```

**While**
El ciclo while se ejecuta mientras una condición sea verdadera.

```python
contador = 0
while contador < 5:
print(contador)
contador += 1 # Incrementar el contador
```

## Iteradores

Un iterador es un objeto que permite recorrer todos los elementos de una colección (como una lista o un string) uno a uno. Python implementa los iteradores usando los métodos **iter**() y **next**().

### Iterar manualmente

Puedes convertir un objeto iterable en un iterador con `iter()`, y luego obtener cada elemento con `next()`.

```python
mi_lista = [10, 20, 30]
mi_iterador = iter(mi_lista)

print(next(mi_iterador)) # Salida: 10
print(next(mi_iterador)) # Salida: 20
print(next(mi_iterador)) # Salida: 30
```

Si se llama a `next()` más veces de las que hay elementos, se lanza una excepción `StopIteration`.

**Definir un iterador personalizado**
Puedes crear un iterador definiendo una clase que implemente los métodos **iter**() y **next**().

```python
class Contador:
def __init__(self, maximo):
self.maximo = maximo
self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.contador < self.maximo:
            self.contador += 1
            return self.contador
        else:
            raise StopIteration

mi_contador = Contador(5)
for numero in mi_contador:
print(numero) # Salida: 1, 2, 3, 4, 5
```

## Funciones

Las funciones permiten agrupar un bloque de código reutilizable que se puede ejecutar llamándola por su nombre. Se definen usando la palabra clave `def`.

```python

# Definición de una función

def saludar():
print("¡Hola!")

# Llamada a la función

saludar() # Salida: ¡Hola!
```

### Funciones con parámetros

Puedes pasar valores (argumentos) a una función para que trabaje con ellos.

```python
def sumar(a, b):
return a + b

resultado = sumar(3, 5) # 8
```

**Parámetros por defecto**
Puedes definir valores predeterminados para los parámetros.

```python
def saludar(nombre="Amigo"):
print("Hola, " + nombre)

saludar("Carlos") # Salida: Hola, Carlos
saludar() # Salida: Hola, Amigo
```

## Lambda

Las funciones lambda son funciones anónimas, es decir, funciones sin nombre que se definen en una sola línea usando la palabra clave lambda. Son útiles para funciones simples que se usan una sola vez.

```python
# Sintaxis de lambda: lambda parámetros: expresión

suma = lambda x, y: x + y

resultado = suma(2, 3) # 5
```

Las lambda suelen usarse en combinación con funciones como `map()`, `filter()`, o `sorted()`.

```python
# Usar lambda con sorted para ordenar por la segunda letra

nombres = ["Ana", "Luis", "Pedro"]
nombres_ordenados = sorted(nombres, key=lambda x: x[1])
print(nombres_ordenados) # Salida: ['Ana', 'Pedro', 'Luis']
```

## Recursividad

La recursividad ocurre cuando una función se llama a sí misma. Es útil para resolver problemas que se pueden descomponer en subproblemas más pequeños. Es importante definir una condición base para evitar recursiones infinitas.

**Ejemplo clásico:** Factorial
El factorial de un número n (denotado como n!) es el producto de todos los números enteros positivos hasta n.

```python
def factorial(n): # Condición base
if n == 1:
return 1 # Llamada recursiva
return n * factorial(n - 1)

resultado = factorial(5) # 5 _ 4 _ 3 _ 2 _ 1 = 120
print(resultado) # Salida: 120
```

**Otro ejemplo:** Fibonacci
La secuencia de Fibonacci es una sucesión en la que cada número es la suma de los dos anteriores.

```python
def fibonacci(n):
if n == 0:
return 0
elif n == 1:
return 1
else:
return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6)) # Salida: 8 (0, 1, 1, 2, 3, 5, 8)
```

## Excepciones

Las excepciones son errores que ocurren durante la ejecución del programa. Python ofrece mecanismos para capturar y manejar estos errores usando `try`, `except`, `else` y `finally`.

### Capturar excepciones

El bloque **try** contiene el código que puede generar una excepción, y **except** define qué hacer si ocurre la excepción.

```python
try: # Código que puede generar un error
resultado = 10 / 0
except ZeroDivisionError: # Qué hacer si ocurre la excepción
print("No se puede dividir entre cero.")
```

### Varios tipos de excepciones

Puedes manejar diferentes tipos de excepciones con múltiples bloques **except**.

```python
try:
numero = int(input("Ingresa un número: "))
resultado = 10 / numero
except ValueError:
print("Eso no es un número válido.")
except ZeroDivisionError:
print("No se puede dividir entre cero.")
```

**Bloques else y finally**

-   El bloque else se ejecuta si no ocurre ninguna excepción.
-   El bloque finally siempre se ejecuta, ocurra o no una excepción, y suele usarse para liberar recursos.

```python
try:
archivo = open("mi_archivo.txt", "r")
contenido = archivo.read()
except FileNotFoundError:
print("El archivo no fue encontrado.")
else:
print("El archivo fue leído exitosamente.")
finally:
archivo.close() # Esto se ejecutará siempre
```
