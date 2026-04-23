from Cuenta import *
from Cliente import *
from Menu import *


class Main:
    pass
# Crear cuenta
cuenta = Cuenta("02/03/2006", "Débito", 95000)

# Crear cliente con su cuenta
cliente = Cliente("Irvin", cuenta)

# Crear menú
menu = Menu("Bienvenido al Banco Rockerin\nElija la opción que desee:")

# Ejecutar sistema
menu.darBienvenida()
menu.despliegaMenu()
menu.procesaOpcion(cliente)
