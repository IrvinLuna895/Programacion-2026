''' 
Created on Abril,2026 
@author: irvinluna

'''

class Cuenta:
    def __init__(self, fechaCreacion, tipoCuenta, saldo):
        self.__fechaCreacion = fechaCreacion
        self.__tipoCuenta = tipoCuenta
        self.__saldo = saldo

    def get_fechaCreacion(self):
        return self.__fechaCreacion

    def get_tipoCuenta(self):
        return self.__tipoCuenta

    def get_saldo(self):
        return self.__saldo

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
            f"Tipo: {self.get_tipoCuenta()} | "
            f"Saldo: {self.get_saldo()} | "
            f"Fecha: {self.get_fechaCreacion()}"
        )
