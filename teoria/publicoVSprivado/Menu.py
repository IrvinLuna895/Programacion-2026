from Cliente import *

class Menu:
    def __init__(self, mensajeDeBienvenida):
        self.mensajeDeBienvenida = mensajeDeBienvenida

    def darBienvenida(self):
        print(self.mensajeDeBienvenida)

    def despliegaMenu(self):
        print("\n1. Depositar")
        print("2. Retirar")
        print("3. Ver información del cliente")
        print("4. Salir")

    def procesaOpcion(self, cliente):
        intentos = 0

        while intentos < 3:
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                if cliente.depositar(cantidad):
                    print("Depósito exitoso.")
                    print(f"Saldo actual: {cliente.get_saldo()}")
                else:
                    print("Error: cantidad inválida.")

            elif opcion == "2":
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                if cliente.retirar(cantidad):
                    print("Retiro exitoso.")
                    print(f"Saldo actual: {cliente.get_saldo()}")
                else:
                    print("Error: fondos insuficientes o cantidad inválida.")

            elif opcion == "3":
                print(cliente)

            elif opcion == "4":
                print("Gracias por usar el sistema.")
                break

            else:
                intentos += 1
                print(f"Opción inválida. Intento {intentos} de 3")

                if intentos == 3:
                    print("Demasiados intentos inválidos.")
