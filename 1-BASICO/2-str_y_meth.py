# Ejemplo de uso de métodos comunes en cadenas y listas en Python

# Variables de ejemplo
mi_string = "  Hola, Mundo  "  # Cadena con espacios al inicio y al final
lista = ["Ángel", "Joan", "Luis", "Carlos"]  # Lista de nombres

# Métodos aplicados sobre la cadena y la lista

# Método len() - Retorna la longitud de la cadena o lista
print("len")
print(len(mi_string))  # Salida: 15 (incluye los espacios en blanco)
print("=" * 15)

# Método lower() - Convierte todos los caracteres de la cadena a minúsculas
print("lower")
print(mi_string.lower())  # Salida: "  hola, mundo  "
print("=" * 15)

# Método upper() - Convierte todos los caracteres de la cadena a mayúsculas
print("upper")
print(mi_string.upper())  # Salida: "  HOLA, MUNDO  "
print("=" * 15)

# Método strip() - Elimina los espacios en blanco al inicio y al final de la cadena
print("strip")
print(mi_string.strip())  # Salida: "Hola, Mundo" (espacios eliminados)
print("=" * 15)

# Método replace() - Reemplaza una subcadena por otra dentro de la cadena
print("replace")
print(mi_string.replace("Hola", "Adiós"))  # Salida: "  Adiós, Mundo  " (se reemplaza "Hola" por "Adiós")
print("=" * 15)

# Método split() - Divide la cadena en una lista de palabras, separando por espacios de forma predeterminada
print("split")
print(mi_string.split())  # Salida: ['Hola,', 'Mundo'] (separa por espacios en blanco)
print("=" * 15)

# Método join() - Une los elementos de una lista en una cadena, usando un delimitador especificado
print("join")
print("-".join(lista))  # Salida: "Ángel-Joan-Luis-Carlos" (une la lista con el delimitador "-")
print("=" * 15)

# Método find() - Busca una subcadena dentro de la cadena y retorna el índice de su primera aparición
print("find")
print(mi_string.find("Mundo"))  # Salida: 8 (el índice donde comienza "Mundo")
print("=" * 15)

# Método startswith() - Verifica si la cadena comienza con una subcadena específica
print("startswith")
print(mi_string.startswith("Hola"))  # Salida: False (la cadena tiene espacios al inicio)
print(mi_string.strip().startswith("Hola"))  # Salida: True (después de usar strip, la cadena empieza con 
                                             #"Hola")
print("=" * 15)

# Método endswith() - Verifica si la cadena termina con una subcadena específica
print("endswith")
print(mi_string.endswith("Mundo"))  # Salida: False (la cadena tiene espacios al final)
print(mi_string.strip().endswith("Mundo"))  # Salida: True (después de usar strip, la cadena termina con 
                                            #"Mundo")
