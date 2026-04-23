from Cuenta import *

class Cliente:
    def __init__(self, nombre, cuenta):
        self.nombre = nombre
        self.cuenta = cuenta  # ← el cliente tiene una cuenta

    def depositar(self, cantidad):
        print(f"\nCliente: {self.nombre}")
        self.cuenta.depositar(cantidad)

    def retirar(self, cantidad):
        print(f"\nCliente: {self.nombre}")
        self.cuenta.retirar(cantidad)

    def mostrarInformacion(self):
        print(f"\n--- Cliente: {self.nombre} ---")
        self.cuenta.mostrarInformacion()
