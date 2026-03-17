from Cuenta import *
from Cliente import *

class Menu:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar(self):
        print(self.mensaje)
        print("1. Depositar")
        print("2. Retirar")
        print("3. Ver cliente")
        print("4. Salir")

    def ejecutar(self, cliente):
        intentos = 0

        while intentos < 3:
            opcion = input("Elige opción: ")

            if opcion == "1":
                cantidad = float(input("Cantidad a depositar: "))
                if cantidad > 0:
                    cliente.cuenta.depositar(cantidad)
                    print("Depósito exitoso")
                else:
                    print("Solo valores positivos")

            elif opcion == "2":
                cantidad = float(input("Cantidad a retirar: "))
                if cantidad > 0 and cantidad <= cliente.cuenta.saldo:
                    cliente.cuenta.retirar(cantidad)
                    print("Retiro exitoso")
                else:
                    print("Cantidad inválida o fondos insuficientes")

            elif opcion == "3":
                print(cliente)

            elif opcion == "4":
                print("Saliendo...")
                break

            else:
                intentos += 1
                print(f"Opción inválida ({intentos}/3)")

        if intentos == 3:
            print("Sistema bloqueado")
