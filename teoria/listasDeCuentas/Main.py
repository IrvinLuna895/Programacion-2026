from Cuenta import *
from Cliente import *
from Menu import *

class Main:
    def ejecutar():
        cliente = Cliente("Irvin", "CDMX", 20)

        c1 = Cuenta("01/01/2024", "Ahorro", 1000)
        c2 = Cuenta("02/02/2024", "Débito", 5000)

        cliente.agregarCuenta(c1)
        cliente.agregarCuenta(c2)

        menu = Menu("Bienvenido al Banco Rockerin")

        menu.darBienvenida()
        menu.despliegaMenu()
        menu.procesaOpcion(cliente)


if __name__ == "__main__":
    Main.ejecutar()
