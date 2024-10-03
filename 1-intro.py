#variables
##declaración
nombre = "Ángel"
edad = 23
altura = 1.72
es_programador = True

#tipos
edad = 30 #int
precio = 12.99 #float
nombre = "Ángel" #string
es_adulto = True #bool
lista_numeros = [1,2,3,4,5] #list
persona = {"nombre": "Ángel", "edad": 23} #dict
nada = None #NoneType

#consejos
##El nombre debe empezar con una letra o un guion bajo (_), pero no con un número.
##Solo puede contener letras, números y guiones bajos.
##Las mayúsculas y minúsculas son diferentes (nombre y Nombre son variables distintas).
##Es preferible usar nombres descriptivos para que tu código sea fácil de entender

#asignación multiple
a, b, c = 10, 20, 30

#intercambio de valor en variables
a, b = b, c

#Tipos de variables mutables e inmutables
##Inmutables: No se pueden cambiar una vez que se han creado (por ejemplo, int, float, str, tuple).
##Mutables: Pueden cambiar su contenido después de ser creados (por ejemplo, list, dict, set).

#conversion de tipos
edad = 23
edad_str = str(edad)

numero = "123"
numero_int = int(123)

altura = 1.72
altura_entero = int(1.72)

#ejemplos
##mostrar información
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Altura: {altura}")
print(f"¿Es programador?: {es_programador}")
print(f"Edad actualizada: {edad + 1}")