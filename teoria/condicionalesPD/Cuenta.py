''' 
Created on Abril,2026 
@author: irvinluna

'''

class Cuenta:
    def __init__(self, fechaCreacion, tipoCuenta, saldo):
        self.fechaCreacion = fechaCreacion
        self.tipoCuenta = tipoCuenta
        self.saldo = saldo

    def __str__(self):
        return (
            "\n--- Información de la cuenta ---\n"
            f"Fecha de creación: {self.fechaCreacion}\n"
            f"Tipo de cuenta: {self.tipoCuenta}\n"
            f"Saldo actual: {self.saldo}"
        )

    def depositar(self, cantidad):
        if cantidad <= 0:
            return False
        self.saldo += cantidad
        return True

    def retirar(self, cantidad):
        if cantidad <= 0:
            return False

        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return True

        return False
