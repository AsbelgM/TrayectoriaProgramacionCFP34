# Import
import math
from ejercicio4 import Punto


# def
class Segmento:
    def __init__(self, puntoA, puntoB):
        self.puntoA = puntoA
        self.puntoB = puntoB

    def __str__(self):
        return "Punto A: {}  Punto B: {}".format(self.puntoA, self.puntoB)

    def set_punto_a(self, nuevoValor):
        self.puntoA =  nuevoValor

    def get_punto_a(self):
        return self.puntoA

    def set_punto_b(self,  nuevoValor):
        self.punto_b =  nuevoValor


    def get_punto_b(self):
        return self.puntoB

    def longitud_segmento(self):
        distancia = math.dist((self.puntoA.x,self.puntoA.y), (self.puntoB.x,self.puntoB.y))
        return distancia
