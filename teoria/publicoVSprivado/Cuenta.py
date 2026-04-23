''' 
Created on Abril,2026 
@author: irvinluna

'''
class Cuenta:
    def __init__(self, fechaCreacion, tipoCuenta, saldo):
        self.__fechaCreacion = fechaCreacion
        self.__tipoCuenta = tipoCuenta
        self.__saldo = saldo

    # GETTERS
    def get_fechaCreacion(self):
        return self.__fechaCreacion

    def get_tipoCuenta(self):
        return self.__tipoCuenta

    def get_saldo(self):
        return self.__saldo

    # MÉTODOS (sin prints)
    def depositar(self, cantidad):
        if cantidad <= 0:
            return False
        self.__saldo += cantidad
        return True

    def retirar(self, cantidad):
        if cantidad <= 0:
            return False
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return True
        return False

    def __str__(self):
        return (
            f"Saldo: {self.get_saldo()} | "
            f"Tipo de cuenta: {self.get_tipoCuenta()} | "
            f"Fecha: {self.get_fechaCreacion()}"
        )
