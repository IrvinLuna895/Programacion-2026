from Cuenta import *
from Cliente import *
from Menu import *

class Main:
  pass
cuenta = Cuenta("02/03/2006", "Débito", 95000)
cliente = Cliente("Irvin Luna", "CDMX", 19, cuenta)

menu = Menu("Bienvenido al Banco Rockerín")
menu.mostrar()
menu.ejecutar(cliente)
