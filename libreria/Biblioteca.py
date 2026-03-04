#Biblioteca.py

class Biblioteca :
  def __init__(self,libros):
        self.libros_disponibles = libros

  def prestar(self,cantidad):
    self.libros_disponibles = self.libros_disponibles - cantidad
    print("Préstamo realizado")


  def devolver(self,cantidad):
    self.libros_disponibles = self.libros_disponibles + cantidad
    print("Libros devueltos correctamente")
