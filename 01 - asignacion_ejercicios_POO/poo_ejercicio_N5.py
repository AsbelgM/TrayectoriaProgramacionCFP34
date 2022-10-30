# Import
import math
from poo_ejercicio_N4 import Punto

# def
class Segmento:
    def __init__(self, puntoA, puntoB):
        self.puntoA = puntoA
        self.puntoB = puntoB

    def __str__(self):
        return "Punto A: {}  Punto B: {}".format(self.puntoA, self.puntoB)

    def set_punto_a(self, valorAsignadoA):
        self.puntoA = valorAsignadoA

    def get_punto_a(self):
        return self.puntoA

    def set_punto_b(self, valorAsignadoB):
        self.punto_b = valorAsignadoB


    def get_punto_b(self):
        return self.puntoB

    def longitud_segmento(self):
        distancia = math.dist([self.puntoA.coordenadaX,self.puntoA.coordenadaY], ([self.puntoB.coordenadaX,self.puntoB.coordenadaY]))
        return distancia