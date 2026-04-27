
from Libro import *

class Biblioteca:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros = []

    def get_nombre(self):
        return self.__nombre

    def get_libros(self):
        return self.__libros

    def agregarLibro(self, libro):
        self.__libros.append(libro)

    def eliminarLibro(self, indice):
        if 0 <= indice < len(self.__libros):
            self.__libros.pop(indice)
            return True
        return False

    def recuperarLibro(self, indice):
        if 0 <= indice < len(self.__libros):
            return self.__libros[indice]
        return None

    def prestarLibro(self, indice):
        libro = self.recuperarLibro(indice)
        if libro:
            return libro.prestar()
        return False

    def devolverLibro(self, indice):
        libro = self.recuperarLibro(indice)
        if libro:
            return libro.devolver()
        return False

    def __str__(self):
        info = f"\nBiblioteca: {self.get_nombre()}\nCatálogo:\n"
        for i, libro in enumerate(self.__libros):
            info += f"[{i}] {libro}\n"
        return info
