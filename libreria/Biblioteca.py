#Biblioteca.py
''' 
Created on March,2026
@author: irvinluna

''' 
class Biblioteca:
    def __init__(self, libros):
        self.libros_disponibles = libros

    def prestar(self, cantidad):
        self.libros_disponibles -= cantidad

    def devolver(self, cantidad):
        self.libros_disponibles += cantidad

    def __str__(self):
        return f"Libros disponibles: {self.libros_disponibles}"
