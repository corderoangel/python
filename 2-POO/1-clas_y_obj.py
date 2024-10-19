class Perro:
    """
    Clase que representa a un perro con atributos y métodos relacionados.
    """

    def __init__(self, nombre, raza):
        """
        Método constructor para inicializar un nuevo objeto Perro.

        Args:
            nombre (str): Nombre del perro.
            raza (str): Raza del perro.
        """
        self.nombre = nombre  # Atributo de instancia
        self.raza = raza  # Atributo de instancia

    def ladrar(self):
        """
        Método que simula el ladrido del perro.
        """
        print(f"{self.nombre} está ladrando.")

    def informacion(self):
        """
        Método que imprime información sobre el perro.
        """
        print(f"El perro se llama {self.nombre} y es de raza {self.raza}.")

# Crear un objeto de la clase Perro
mi_perro = Perro("Fido", "Labrador")

# Llamar a los métodos del objeto
mi_perro.ladrar()  # Fido está ladrando.
mi_perro.informacion()  # El perro se llama Fido y es de raza Labrador.
