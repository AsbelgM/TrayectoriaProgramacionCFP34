
class Carta:

    def __init__(self,valor,simbolo):
        self.valor = valor
        self.simbolo = simbolo

    def es_uno_de_oro(self):
        if str(self.valor) + self.simbolo == "1o":
            return True

    def __str__(self):
        return "{} {}".format (self.valor,self.simbolo)

class Mazo:
    simbolos = ["oros", "espadas", "bastos", "copas"]
    valores = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    def __init__(self,cantidad_cartas,simbolos):
        self.cantidad_cartas = cantidad_cartas
        self.simbolos = simbolos
        self.baraja = []
        i=0
    def crear_mazo(self):
        for i in self.simbolos:
            for n in self.valores:
                carta = "{} {}".format(n,i)
                self.baraja.append(carta)
