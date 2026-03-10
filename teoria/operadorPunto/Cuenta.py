#Cuenta.py

class Cuenta :
  def __init__(self,valor,taip,fecha):
    self.saldo = valor
    self.tipo = taip
    self.fechaCreacion = fecha

  def depositar(self,cantidad):
    self.saldo = self.saldo + cantidad

  def retirar(self,cantidad):
    self.saldo= self.saldo - cantidad

  def informacion(self):
    print("El saldo de tu cuenta es:", self.saldo)
    print("El tipo de cuenta es:", self.tipo)
    print("La fecha de creacion de la cuenta es:", self.fechaCreacion)
