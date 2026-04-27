



class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = disponible

    # GETTERS
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_disponible(self):
        return self.__disponible

    # MÉTODOS
    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def devolver(self):
        if not self.__disponible:
            self.__disponible = True
            return True
        return False

    def __str__(self):
        estado = "Disponible" if self.get_disponible() else "Prestado"
        return f"{self.get_titulo()} - {self.get_autor()} ({estado})"
