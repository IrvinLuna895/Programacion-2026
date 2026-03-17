from biblioteca import Biblioteca
from cliente import Cliente
from menu import Menu


class Main:
  pass

def main():
    biblioteca = Biblioteca(50)
    cliente = Cliente("Irvin", 20, biblioteca)

    menu = Menu(" Bienvenido al sistema de Biblioteca")
    menu.mostrar()
    menu.ejecutar(cliente)

if __name__ == "__main__":
    main()
