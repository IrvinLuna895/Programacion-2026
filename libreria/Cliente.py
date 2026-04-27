
class Cliente:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__librosPrestados = []

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_librosPrestados(self):
        return self.__librosPrestados

    def agregarPrestamo(self, libro):
        self.__librosPrestados.append(libro)

    def devolverPrestamo(self, libro):
        if libro in self.__librosPrestados:
            self.__librosPrestados.remove(libro)
            return True
        return False

    def __str__(self):
        info = f"\nCliente: {self.get_nombre()} | Edad: {self.get_edad()}\n"
        info += "Libros prestados:\n"

        if not self.__librosPrestados:
            info += "Ninguno\n"
        else:
            for libro in self.__librosPrestados:
                info += f"- {libro.get_titulo()}\n"

        return info
