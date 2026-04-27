from Biblioteca import *
from Cliente import *
from Libro import *

class Menu:
    def __init__(self, mensaje):
        self.__mensaje = mensaje

    def mostrar(self):
        print(self.__mensaje)
        print("1. Ver catálogo")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Agregar libro")
        print("5. Eliminar libro")
        print("6. Ver cliente")
        print("7. Salir")

    def seleccionarLibro(self, biblioteca):
        while True:
            print(biblioteca)

            try:
                indice = int(input("Seleccione el índice del libro: "))

                if 0 <= indice < len(biblioteca.get_libros()):
                    return indice
                else:
                    print("Índice inválido.")

            except ValueError:
                print("Ingrese un número válido.")

    def ejecutar(self, cliente, biblioteca):
        intentos = 0

        while intentos < 3:
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(biblioteca)

            elif opcion == "2":
                indice = self.seleccionarLibro(biblioteca)
                libro = biblioteca.recuperarLibro(indice)

                if biblioteca.prestarLibro(indice):
                    cliente.agregarPrestamo(libro)
                    print("Préstamo realizado.")
                else:
                    print("No se pudo prestar.")

            elif opcion == "3":
                indice = self.seleccionarLibro(biblioteca)
                libro = biblioteca.recuperarLibro(indice)

                if biblioteca.devolverLibro(indice):
                    cliente.devolverPrestamo(libro)
                    print("Devolución realizada.")
                else:
                    print("No se pudo devolver.")

            elif opcion == "4":
                titulo = input("Título: ")
                autor = input("Autor: ")
                biblioteca.agregarLibro(Libro(titulo, autor))
                print("Libro agregado.")

            elif opcion == "5":
                indice = self.seleccionarLibro(biblioteca)

                if biblioteca.eliminarLibro(indice):
                    print("Libro eliminado.")
                else:
                    print("No se pudo eliminar.")

            elif opcion == "6":
                print(cliente)

            elif opcion == "7":
                print("Saliendo...")
                break

            else:
                intentos += 1
                print(f"Opción inválida ({intentos}/3)")

                if intentos == 3:
                    print("Sistema bloqueado.")
