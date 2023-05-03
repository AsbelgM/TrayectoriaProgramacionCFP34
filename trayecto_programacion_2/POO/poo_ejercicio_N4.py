# Import
import math


# def
class Punto:
    def __init__(self, coordenadaX, coordenadaY):
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY

    def cuadrante(self):
        if self.coordenadaX > 0 and self.coordenadaY > 0:
            return 1
        else:
            if self.coordenadaX < 0 and self.coordenadaY > 0:
                return 2
            else:
                if self.coordenadaX > 0 and self.coordenadaY < 0:
                    return 4
                else:
                    return 3

    def __eq__(self, other):
        return self.coordenadaX == other.coordenadaX and self.coordenadaY == other.coordenadaY

    def distancia_al_centro(self):
        coordenada = (self.coordenadaX, self.coordenadaY)
        centro = (0, 0)
        distancia = math.dist(centro, coordenada)
        return distancia

    def __str__(self):
        return "Punto en " + "(" + str(self.coordenadaX) + "," + str(self.coordenadaY) + ")"
