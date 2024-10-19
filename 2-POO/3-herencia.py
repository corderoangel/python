class Animal:
    """
    Clase base que representa un animal genérico.
    """

    def __init__(self, nombre):
        """
        Método constructor para inicializar un nuevo animal.

        Args:
            nombre (str): Nombre del animal.
        """
        self.nombre = nombre

    def sonido(self):
        """
        Método que simula un sonido de un animal. Se sobrescribe en las subclases.
        """
        raise NotImplementedError("Este método debe ser sobrescrito por subclases.")


class Gato(Animal):
    """
    Clase que representa a un gato, hereda de la clase Animal.
    """

    def sonido(self):
        """
        Método sobrescrito que simula el sonido de un gato.
        """
        return "Miau"


class Perro(Animal):
    """
    Clase que representa a un perro, hereda de la clase Animal.
    """

    def sonido(self):
        """
        Método sobrescrito que simula el sonido de un perro.
        """
        return "Guau"


# Crear objetos de las clases derivadas
gato = Gato("Michi")
perro = Perro("Firulais")

# Llamar al método sobrescrito en cada objeto
print(f"{gato.nombre} dice {gato.sonido()}")  # Michi dice Miau
print(f"{perro.nombre} dice {perro.sonido()}")  # Firulais dice Guau
