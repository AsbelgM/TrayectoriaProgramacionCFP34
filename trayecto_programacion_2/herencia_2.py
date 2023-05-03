class Vehiculo: #clase padre Vehiculo
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def get_ruedas(self):
        return int(self.ruedas)

    def get_color(self):
        return self.color


class Coche(Vehiculo): #clase hijo coche

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def get_velocidad(self):
        return float(self.velocidad)

    def get_cilindrada(self):
        return int(self.cilindrada)
