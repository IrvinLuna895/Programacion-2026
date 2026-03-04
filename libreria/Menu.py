#Menu.py
#from Biblioteca import

class Menu :
  pass
print("Desde el Menu")
biblioteca1 = Biblioteca(50)
print("Esta es la cantidad de libros disponibles:", biblioteca1.libros_disponibles)

biblioteca1.prestar(22)

print("Probando el prestamo")
print("Después del prestamo, los libros disponibles son:", biblioteca1.libros_disponibles) #28

biblioteca1.devolver(12)

print("Probando la devolución")
print("Después de devolverse los libros, la cantidad disponible es:", biblioteca1.libros_disponibles) #40
