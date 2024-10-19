a = [1, 2, 3, 4, 5]  # Lista original
b = a  # Asignación directa: b apunta al mismo objeto que a
print(a)  # Imprime: [1, 2, 3, 4, 5]
print(b)  # Imprime: [1, 2, 3, 4, 5]

del a[0]  # Elimina el primer elemento de la lista 'a'
print(id(a))  # Imprime el identificador único del objeto 'a' en memoria
print(id(b))  # Imprime el mismo identificador que 'a', ya que ambos apuntan al mismo objeto

c = a[:]  # Crea una copia superficial de 'a'
print(id(a))  # Identificador de 'a'
print(id(b))  # Identificador de 'b', igual al de 'a'
print(id(c))  # Identificador de 'c', diferente, ya que es una nueva lista

a.append(6)  # Agrega el número 6 al final de la lista 'a'
print(a)  # Imprime: [2, 3, 4, 5, 6]
print(b)  # Imprime: [2, 3, 4, 5, 6], ya que 'b' aún es una referencia de 'a'
print(c)  # Imprime: [2, 3, 4, 5], ya que 'c' es una copia independiente
