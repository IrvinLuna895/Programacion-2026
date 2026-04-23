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
            print("Error: la cantidad debe ser mayor que 0.")
            return

        self.saldo += cantidad
        print("Depósito exitoso. Nuevo saldo:", self.saldo)

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que 0.")
            return

        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print("Retiro exitoso. Nuevo saldo:", self.saldo)
        else:
            print("Fondos insuficientes.")
