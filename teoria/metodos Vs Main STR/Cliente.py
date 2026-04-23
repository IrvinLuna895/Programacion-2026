
from Cuenta import *

class Cliente:
    def __init__(self, nombre, cuenta):
        self.nombre = nombre
        self.cuenta = cuenta

    def __str__(self):
        return (
            f"\n--- Cliente: {self.nombre} ---\n"
            f"{self.cuenta}"
        )

    def depositar(self, cantidad):
        print(f"\nCliente: {self.nombre}")
        self.cuenta.depositar(cantidad)

    def retirar(self, cantidad):
        print(f"\nCliente: {self.nombre}")
        self.cuenta.retirar(cantidad)
