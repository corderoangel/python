try:
    # Solicita al usuario que ingrese un número divisor
    divisor = int(input("Ingresa un número divisor: "))
    
    # Calcula el resultado de la división
    result = 100 / divisor
    
    # Imprime el resultado de la división
    print(result)

except ZeroDivisionError as e:
    # Maneja la excepción cuando el divisor es cero
    print("Error: El divisor no puede ser cero.")
    print("Ha ocurrido un error:", e)

except ValueError as e:
    # Maneja la excepción cuando la entrada no es un número válido
    print("Error: Debes introducir un número válido.")
    print("Ha ocurrido un error:", e)

# Función comentada para imprimir la jerarquía de excepciones
# def print_exception_hierarchy(exception_class, indent=0):
#     """
#     Imprime la jerarquía de excepciones, mostrando la relación entre
#     las clases de excepciones y sus subclases.

#     Args:
#         exception_class (Exception): Clase de excepción a imprimir.
#         indent (int): Nivel de indentación para la visualización jerárquica.
#     """
#     print(' ' * indent + exception_class.__name__)
#     for subclass in exception_class.__subclasses__():
#         print_exception_hierarchy(subclass, indent + 4)

# Llamada comentada a la función para imprimir la jerarquía de excepciones
# print_exception_hierarchy(Exception)
