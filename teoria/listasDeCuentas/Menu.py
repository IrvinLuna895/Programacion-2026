from Cliente import *

class Menu:
    def __init__(self, mensajeDeBienvenida):
        self.mensajeDeBienvenida = mensajeDeBienvenida

    def darBienvenida(self):
        print(self.mensajeDeBienvenida)

    def despliegaMenu(self):
        print("\n1. Depositar")
        print("2. Retirar")
        print("3. Ver cuentas")
        print("4. Salir")

    def seleccionarCuenta(self, cliente):
        cuentas = cliente.get_cuentas()

        if not cuentas:
            print("No hay cuentas disponibles.")
            return None

        while True:
            print("\nCuentas disponibles:")
            for i, cuenta in enumerate(cuentas):
                print(f"[{i}] {cuenta}")

            try:
                indice = int(input("Seleccione el índice de la cuenta: "))

                if 0 <= indice < len(cuentas):
                    return indice
                else:
                    print("Error: índice fuera de rango.")

            except ValueError:
                print("Error: debe ingresar un número.")

    def pedirCantidad(self, mensaje):
        while True:
            try:
                cantidad = float(input(mensaje))
                return cantidad
            except ValueError:
                print("Error: debe ingresar un número válido.")

    def procesaOpcion(self, cliente):
        intentos = 0

        while intentos < 3:
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                indice = self.seleccionarCuenta(cliente)
                if indice is None:
                    continue

                cantidad = self.pedirCantidad("Cantidad a depositar: ")

                if cliente.depositar(indice, cantidad):
                    cuenta = cliente.recuperarCuenta(indice)
                    print("Depósito exitoso.")
                    print(f"Saldo actual: {cuenta.get_saldo()}")
                else:
                    print("Error: cantidad inválida.")

            elif opcion == "2":
                indice = self.seleccionarCuenta(cliente)
                if indice is None:
                    continue

                cantidad = self.pedirCantidad("Cantidad a retirar: ")

                if cliente.retirar(indice, cantidad):
                    cuenta = cliente.recuperarCuenta(indice)
                    print("Retiro exitoso.")
                    print(f"Saldo actual: {cuenta.get_saldo()}")
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
