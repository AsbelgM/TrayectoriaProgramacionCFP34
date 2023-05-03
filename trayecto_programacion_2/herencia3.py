# import
import herencia_3_1


# Main

class Coche(herencia_3_1.Vehiculo_a_motor):

    def __init__(self, color, ruedas, velocidad, distanciaRecorrida, tanque, cilindrada):
        herencia_3_1.Vehiculo_a_motor.__init__(self, color, ruedas, velocidad, distanciaRecorrida, tanque, cilindrada)


class Bicicleta(herencia_3_1.Vehiculo):

    def __init__(self, color, ruedas, velocidad, tipo):
        herencia_3_1.Vehiculo.__init__(self, color, ruedas, velocidad)
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo


class Motocicleta(herencia_3_1.Vehiculo_a_motor):

    def __init__(self, color, ruedas, velocidad, distanciaRecorrida, tanque, cilindrada):
        herencia_3_1.Vehiculo_a_motor.__init__(self, color, ruedas, velocidad, distanciaRecorrida, tanque, cilindrada)


class Camioneta(herencia_3_1.Vehiculo_a_motor):
    def __init__(self, color, ruedas, velocidad, distanciaRecorrida, tanque, cilindrada, carga):
        herencia_3_1.Vehiculo_a_motor.__init__(self, color, ruedas, velocidad, distanciaRecorrida, tanque, cilindrada)
        self.carga = carga

    def get_carga(self):
        return self.carga


tanque = herencia_3_1.Tanque(combustible=100, relacionConsumoDistancia=0.5)

auto = Coche(color="rojo", ruedas=4, velocidad=120, distanciaRecorrida=10, tanque=tanque, cilindrada=4)

