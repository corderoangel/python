# Definición de funciones matemáticas

def add(a, b):
    """
    Suma dos números.

    :param a: Primer número a sumar.
    :param b: Segundo número a sumar.
    :return: La suma de a y b.
    """
    return a + b

def substract(a, b):
    """
    Resta dos números.

    :param a: Minuendo.
    :param b: Sustraendo.
    :return: La diferencia de a y b.
    """
    return a - b

def multiply(a, b):
    """
    Multiplica dos números.

    :param a: Primer número a multiplicar.
    :param b: Segundo número a multiplicar.
    :return: El producto de a y b.
    """
    return a * b

def divide(a, b):
    """
    Divide dos números.

    :param a: Dividendo.
    :param b: Divisor.
    :return: El cociente de a y b.
    :raises ZeroDivisionError: Si b es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b

def calculator():
    """
    Función que permite al usuario realizar operaciones aritméticas básicas.

    Este bucle interactivo solicita al usuario que seleccione una operación,
    ingrese dos números y muestra el resultado de la operación seleccionada.
    El bucle continúa hasta que el usuario decide salir.
    """
    while True:
        # Presentar el menú de operaciones al usuario
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        # Leer la opción del usuario
        option = input("Ingrese su opción (1, 2, 3, 4, 5): ")

        # Salir del bucle si el usuario elige salir
        if option == "5":
            print("Saliendo de la calculadora")
            break

        # Verificar que la opción elegida es válida
        if option in ["1", "2", "3", "4"]:
            # Leer los números de entrada
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            # Realizar la operación correspondiente y mostrar el resultado
            if option == "1":
                print("La suma es:", add(num1, num2))
            elif option == "2":
                print("La resta es:", substract(num1, num2))
            elif option == "3":
                print("La multiplicación es:", multiply(num1, num2))
            elif option == "4":
                try:
                    print("La división es:", divide(num1, num2))
                except ZeroDivisionError as e:
                    print(e)
        
        else:
            # Manejar opciones no válidas
            print("Opción no válida, por favor intenta de nuevo.")

# Llamar a la función calculadora para iniciar la aplicación
calculator()
