from Cuenta import *
from Cliente import *
from Menu import *



cuenta = Cuenta("02/03/2006", "Débito", 95000)
cliente = Cliente("Irvin", cuenta)

menu = Menu("Bienvenido al Banco Rockerin\nElija la opción que desee:")

menu.darBienvenida()
menu.despliegaMenu()
menu.procesaOpcion(cliente)
