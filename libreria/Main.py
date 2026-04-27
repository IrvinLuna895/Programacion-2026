from Libro import *
from Biblioteca import *
from Cliente import *
from Menu import *

class Main:
    pass


def main():
    biblioteca = Biblioteca("Biblioteca Central")

    biblioteca.agregarLibro(Libro("1984", "George Orwell"))
    biblioteca.agregarLibro(Libro("Cien años de soledad", "Gabriel García Márquez"))
    biblioteca.agregarLibro(Libro("El Principito", "Antoine de Saint-Exupéry"))

    cliente = Cliente("Irvin", 20)

    menu = Menu("Bienvenido al Sistema de Biblioteca 'Enjambre' ")

    menu.mostrar()
    menu.ejecutar(cliente, biblioteca)


if __name__ == "__main__":
    main()
