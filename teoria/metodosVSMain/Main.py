from Cuenta import *
from Menu import *


class Main:
    pass


# Ejecución
menu = Menu("Bienvenido al Banco Rockerin\nEliga la opción que desee:")
cuenta = Cuenta("02/03/2006", "Débito", 95000)

menu.darBienvenida()
menu.despliegaMenu()
menu.procesaOpcion(cuenta)
