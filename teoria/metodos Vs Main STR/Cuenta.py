class Cuenta:
    def __init__(self, fechaCreacion, tipoCuenta, saldo):
        self.fechaCreacion = fechaCreacion
        self.tipoCuenta = tipoCuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        self.saldo -= cantidad

    def __str__(self):
        return f"Saldo: {self.saldo} | Tipo de cuenta: {self.tipoCuenta} | Fecha: {self.fechaCreacion}"
