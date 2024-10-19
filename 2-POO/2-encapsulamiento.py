class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria con saldo privado.
    """

    def __init__(self, titular, saldo):
        """
        Método constructor para inicializar una nueva cuenta bancaria.

        Args:
            titular (str): Nombre del titular de la cuenta.
            saldo (float): Saldo inicial de la cuenta.
        """
        self.titular = titular
        self._saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        """
        Método para depositar una cantidad en la cuenta.

        Args:
            cantidad (float): Cantidad a depositar.
        """
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self._saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def obtener_saldo(self):
        """
        Método para obtener el saldo actual de la cuenta.

        Returns:
            float: El saldo actual de la cuenta.
        """
        return self._saldo

# Crear un objeto de la clase CuentaBancaria
mi_cuenta = CuentaBancaria("Juan", 1000)

# Hacer un depósito
mi_cuenta.depositar(500)  # Depósito exitoso. Nuevo saldo: 1500

# Obtener el saldo actual
print(f"Saldo disponible: {mi_cuenta.obtener_saldo()}")  # Saldo disponible: 1500
