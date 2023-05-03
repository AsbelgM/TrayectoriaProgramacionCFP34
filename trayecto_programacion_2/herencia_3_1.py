#def
class Vehiculo:  #clase que contiene caracteristicas generales del vehiculo
    def __init__(self, color, ruedas, velocidad):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad

    def get_ruedas(self):
        return self.ruedas

    def get_color(self):
        return self.color

    def get_velocidad(self):
        return self.velocidad


class Tanque: #clase tanque para vehiculos con motor
    def __init__(self, combustible, relacionConsumoDistancia):
        self.combustible = combustible
        self.relacionConsumoDistancia = relacionConsumoDistancia

    def cargar_combustible(self, cantidadCombustible): #cargamos combustible al vehiculo
        self.combustible += cantidadCombustible
        return "La capacidad del tanque es de: {} Litros, se ha cargado combustible ".format(self.combustible)

    def recorrer_distancia(self, distancia): #consumo de combustibe en relacion a distancia
        autonomia = float(distancia * self.relacionConsumoDistancia)
        if autonomia < self.combustible:
            self.combustible -= autonomia
            distancia += distancia
            return "El vehiculo posee {} listros de combustible, ha recorrido una distancia de {} KMS".format(
                self.combustible, distancia)
        else:
            return str("No posee combustible para realizar el viaje")


class Vehiculo_a_motor(Vehiculo): #clase que hereda de la clase vehiculo y se añade caracteristicas del motor y un objeto tanque

    def __init__(self, color, ruedas, velocidad, distanciaRecorrida, tanque, cilindrada):
        Vehiculo.__init__(self, color, ruedas, velocidad)
        self.distanciaRecorrida = distanciaRecorrida
        self.tanque = tanque
        self.cilindrada = cilindrada

    def get_distanciaRecorrida(self):
        return self.distanciaRecorrida

    def get_cilinrada(self):
        return self.cilindrada
