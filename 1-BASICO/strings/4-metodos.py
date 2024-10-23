#.upper() y .lower()
s = "Python"
print(s.upper())  # Salida: PYTHON
print(s.lower())  # Salida: python

#.capitalize()
s = "python"
print(s.capitalize())  # Salida: Python

#.strip(), .lstrip(), y .rstrip()
s = "  Hola  "
print(s.strip())  # Salida: Hola
print(s.lstrip()) # Salida: 'Hola  ' (elimina espacios a la izquierda)
print(s.rstrip()) # Salida: '  Hola' (elimina espacios a la derecha)

#.replace()
s = "Hola Mundo"
s_modificada = s.replace("Mundo", "Python")
print(s_modificada)  # Salida: Hola Python

#.split() y .join()
s = "Hola, Mundo, Python"
partes = s.split(", ")
print(partes)  # Salida: ['Hola', 'Mundo', 'Python']

lista = ["Hola", "Mundo", "Python"]
unido = " ".join(lista)
print(unido)  # Salida: Hola Mundo Python

#.find() y .index()
s = "Hola Mundo"
print(s.find("Mundo"))  # Salida: 5
print(s.index("Mundo")) # Salida: 5
# print(s.find("Python"))  # Salida: -1
# print(s.index("Python")) # Error: ValueError

#Comprobaciones con Strings
s = "Python"
print(s.isalpha())  # Salida: True
s = "12345"
print(s.isdigit())  # Salida: True
s = "Python123"
print(s.isalnum())  # Salida: True

#Formateo de Strings
nombre = "Carla"
edad = 25
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje)  # Salida: Hola, mi nombre es Carla y tengo 25 años.

#Método .format()
mensaje = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(mensaje)  # Salida: Hola, mi nombre es Carla y tengo 25 años.

#Operador % (estilo antiguo)
mensaje = "Hola, mi nombre es %s y tengo %d años." % (nombre, edad)
print(mensaje)  # Salida: Hola, mi nombre es Carla y tengo 25 años.

#Escapado de caracteres especiales
comillas = 'Este es un string con comillas simples \'y\' dobles \"'
print(comillas)

#Raw Strings
ruta = r"C:\nueva\carpeta"
print(ruta)  # Salida: C:\nueva\carpeta (el \n no es interpretado como nueva línea)

#Comparación de Strings
print("Python" == "python")  # Salida: False (las mayúsculas y minúsculas son diferentes)
print("abc" < "def")  # Salida: True (la comparación se basa en el valor ASCII)
