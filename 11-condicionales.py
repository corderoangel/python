# Ejemplo de uso de estructuras de control: condicionales

# 1. Comparación simple de un valor
x = 5  # Asignación de un valor a x
if x > 5:
    print("X es mayor que 5")  # Mensaje si x es mayor que 5
elif x == 5:
    print("X es igual que 5")  # Mensaje si x es igual a 5
else:
    print("X es menor que 5")  # Mensaje si x es menor que 5
print("afuera")  # Mensaje que se imprime siempre al final

# 2. Comparaciones utilizando operadores lógicos
x = 15  # Asignación de un valor a x
y = 20  # Asignación de un valor a y

# Comprobación de que x es mayor que 10 y y es mayor que 25
if x > 10 and y > 25:
    print("X es mayor que 10 y Y es mayor que 15")  # Mensaje si ambas condiciones son verdaderas

# Comprobación de que x es mayor que 10 o y es mayor que 25
if x > 10 or y > 25:
    print("X es mayor que 10 O Y es Mayor que 25")  # Mensaje si al menos una condición es verdadera

# Comprobación de que x no es mayor que 10
if not x > 10:
    print("X no es mayor que 10")  # Mensaje si la condición es falsa

# 3. Uso de estructuras anidadas
is_member = True  # Estado de membresía
age = 11  # Edad del usuario

# Comprobación del estado de membresía
if is_member:
    if age >= 15:
        print("Tienes acceso ya que eres miembro y mayor o igual a 15 años")  # Mensaje si es miembro y mayor de 15
    else:
        print("No tienes acceso ya que eres miembro pero menor a 15 años")  # Mensaje si es miembro pero menor de 15
else:
    print("No eres miembro y NO TIENES ACCESO")  # Mensaje si no es miembro
