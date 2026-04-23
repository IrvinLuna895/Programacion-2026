from Cuenta import *

class Menu:
    def __init__(self, mensajeDeBienvenida):
        self.mensajeDeBienvenida = mensajeDeBienvenida

    def darBienvenida(self):
        print(self.mensajeDeBienvenida)

    def despliegaMenu(self):
        print("\n1. Depositar")
        print("2. Retirar")
        print("3. Ver información de la cuenta")
        print("4. Salir")

    def procesaOpcion(self, cuenta):

        intentos = 0

        while intentos < 3:

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print("Estás en la opción de Depositar")
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                cuenta.depositar(cantidad)

            elif opcion == "2":
                print("Estás en la opción de Retirar")
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cuenta.retirar(cantidad)

            elif opcion == "3":
                cuenta.mostrarInformacion()

            elif opcion == "4":
                print("Gracias por usar el sistema bancario rockerin, vuelva pronto.")
                break

            else:
                intentos += 1
                print("Opción inválida. Intento", intentos, "de 3")

                if intentos == 3:
                    print("Demasiados intentos inválidos. El sistema se cerrará.")
