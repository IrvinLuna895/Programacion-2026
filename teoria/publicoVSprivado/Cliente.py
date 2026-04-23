from Cuenta import *

class Cliente:
    def __init__(self, nombre, direccion, edad, cuenta):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.__cuenta = cuenta

    # GETTERS
    def get_nombre(self):
        return self.__nombre

    def get_direccion(self):
        return self.__direccion

    def get_edad(self):
        return self.__edad

    def get_cuenta(self):
        return self.__cuenta

    def get_saldo(self):
        return self.__cuenta.get_saldo()

    # MÉTODOS
    def depositar(self, cantidad):
        return self.__cuenta.depositar(cantidad)

    def retirar(self, cantidad):
        return self.__cuenta.retirar(cantidad)

    def __str__(self):
        return (
            f"\nNombre: {self.get_nombre()}\n"
            f"Dirección: {self.get_direccion()}\n"
            f"Edad: {self.get_edad()}\n"
            f"{self.get_cuenta()}"
        )
