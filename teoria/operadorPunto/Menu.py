#Menu.py
#from cuenta import

class Menu :
  pass
print("Desde el Menu")
cuenta1 = Cuenta(3000,"DEBITO","02/03/2010")
cuenta1.informacion()


cuenta2 = Cuenta(5000,"CREDITO","09/10/1999")
cuenta2.informacion()

cuenta1.depositar(5000)

print("Probando el deposito")
print("Este es tu nuevo saldo en  la cuenta 1:", cuenta1.saldo) #8000

cuenta1.retirar(1200)

print("Probando el retiro")
print("Este es tu nuevo saldo:", cuenta1.saldo) #6800

