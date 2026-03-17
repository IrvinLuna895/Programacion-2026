from Biblioteca import *
from Cliente import *


class Menu:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar(self):
        print(self.mensaje)
        print("1. Prestar libros")
        print("2. Devolver libros")
        print("3. Ver cliente y biblioteca")
        print("4. Salir")

    def ejecutar(self, cliente):
        intentos = 0

        while intentos < 3:
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                cantidad = int(input("¿Cuántos libros quieres prestar?: "))
                if cantidad > 0 and cantidad <= cliente.biblioteca.libros_disponibles:
                    cliente.biblioteca.prestar(cantidad)
                    print("Préstamo realizado")
                else:
                    print("Cantidad inválida o no hay suficientes libros")

            elif opcion == "2":
                cantidad = int(input("¿Cuántos libros quieres devolver?: "))
                if cantidad > 0:
                    cliente.biblioteca.devolver(cantidad)
                    print("Devolución realizada")
                else:
                    print("Cantidad inválida")

            elif opcion == "3":
                print("\n--- Información del cliente ---")
                print(cliente)

            elif opcion == "4":
                print("Saliendo...")
                break

            else:
                intentos += 1
                print(f"Opción inválida ({intentos}/3)")

        if intentos == 3:
            print("Sistema bloqueado")
