from Cuenta import *
from Cliente import *
from Menu import *


class Main:

   
   
   def ejecutar():
        cuenta = Cuenta("02/03/2006", "Débito", 95000)
        cliente = Cliente("Irvin", "CDMX", 20, cuenta)

        menu = Menu("Bienvenido al Banco Rockerin")

        menu.darBienvenida()
        menu.despliegaMenu()
        menu.procesaOpcion(cliente)


if __name__ == "__main__":
    Main.ejecutar()
