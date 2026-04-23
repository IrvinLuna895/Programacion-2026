from Cuenta import *

class Cliente:
    def __init__(self, nombre, direccion, edad):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.__cuentas = []

    def get_nombre(self):
        return self.__nombre

    def get_cuentas(self):
        return self.__cuentas

    def agregarCuenta(self, cuenta):
        self.__cuentas.append(cuenta)

    def borrarCuenta(self, indice):
        if 0 <= indice < len(self.__cuentas):
            self.__cuentas.pop(indice)
            return True
        return False

    def recuperarCuenta(self, indice):
        if 0 <= indice < len(self.__cuentas):
            return self.__cuentas[indice]
        return None

    def depositar(self, indice, cantidad):
        cuenta = self.recuperarCuenta(indice)
        if cuenta:
            return cuenta.depositar(cantidad)
        return False

    def retirar(self, indice, cantidad):
        cuenta = self.recuperarCuenta(indice)
        if cuenta:
            return cuenta.retirar(cantidad)
        return False

    def __str__(self):
        info = f"\nCliente: {self.__nombre}\nCuentas:\n"
        for i, cuenta in enumerate(self.__cuentas):
            info += f"[{i}] {cuenta}\n"
        return info
