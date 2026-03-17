''' 
Created on March,2026
@author: irvinluna

''' 

from Cuenta import *

class Cliente:
    def __init__(self, nombre, direccion, edad, cuenta):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.cuenta = cuenta  

    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Dirección: {self.direccion}\n"
                f"Edad: {self.edad}\n"
                f"{self.cuenta}") 
