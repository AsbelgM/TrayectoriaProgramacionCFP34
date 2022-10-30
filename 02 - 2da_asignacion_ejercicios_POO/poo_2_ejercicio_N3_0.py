# import
import random


# def

class Carta:  # creamos la clase carta
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def es_uno_de_oro(self):
        if self.valor == "1" and self.palo == "ORO":
            return True
        else:
            return False

    def __str__(self):
        return "{}{}".format(self.valor, self.palo)


class Baraja:  # creamos la clase baraja
    def __init__(self):
        self.cartas = []

    def crear_baraja(self):  # creamos la baraja
        valor = ["1", "2", "3", "4", "5", "6", "7", "10", "11", "12"]
        palos = ["ORO", "ESPADAS", "COPAS", "BASTOS"]
        for i in valor:
            for j in palos:
                carta = Carta(i, j)  # cada item de la clase baraja sera un objeto de la clase Carta
                self.cartas.append(carta)

    def sacar_carta(self):
        return self.cartas.pop(0)

    def mostrar_cartas(self):
        for elemento in self.cartas:
            print(elemento)

    def mezclar_cartas(self):
        random.shuffle(self.cartas)

    def reiniciar_cartas(self):
        self.cartas.clear()
        self.crear_baraja()
