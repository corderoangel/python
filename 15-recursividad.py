def sum_numbers(n):
    """
    Calcula la suma de los primeros n números enteros de forma recursiva.

    Args:
        n (int): Un número entero no negativo.

    Returns:
        int: La suma de los primeros n números enteros.
    
    Raises:
        ValueError: Si n es un número negativo.
    """
    
    # Verifica si el número es negativo y lanza una excepción
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
    
    # Caso base: si n es 0, la suma es 0
    if n == 0:
        return 0
    
    # Caso recursivo: n + suma de (n-1)
    else:
        return n + sum_numbers(n - 1)

# Llamada a la función para calcular la suma de los primeros 5 números
result = sum_numbers(5)
# Imprimir el resultado
print(f"Suma de los primeros 5 números es: {result}")
