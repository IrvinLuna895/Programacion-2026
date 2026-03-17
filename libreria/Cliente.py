class Cliente:
    def __init__(self, nombre, edad, biblioteca):
        self.nombre = nombre
        self.edad = edad
        self.biblioteca = biblioteca

    def __str__(self):
        return (f"Cliente: {self.nombre}\n"
                f"Edad: {self.edad}\n"
                f"{self.biblioteca}")  # llama al str de Biblioteca
