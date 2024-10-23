s1 = "Hola"
s2 = "Mundo"

#Concatenación
resultado = s1 + " " + s2
print(resultado)  # Salida: Hola Mundo

#Repetición
repetido = "Hola " * 3
print(repetido)  # Salida: Hola Hola Hola

#Longitud
mi_string = "Python"
print(len(mi_string))  # Salida: 6

#Indexación
mi_string = "Python"
print(mi_string[0])  # Salida: P
print(mi_string[-1])  # Salida: n (índice negativo cuenta desde el final)

#Slicing (rebanado)
mi_string = "Python"
print(mi_string[0:4])  # Salida: Pyth (desde el índice 0 hasta el 3)
print(mi_string[1:])   # Salida: ython (desde el índice 1 hasta el final)
print(mi_string[:3])   # Salida: Pyt (desde el inicio hasta el índice 2)
print(mi_string[::-1]) # Salida: nohtyP (cadena invertida)
