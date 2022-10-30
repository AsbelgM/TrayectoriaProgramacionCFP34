# import
import random


# def
class Carta:  # creamos la clase carta
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return "{}-{}".format(self.valor, self.palo)


class Baraja:  # creamos la clase baraja
    def __init__(self):
        valor = ["1", "2", "3", "4", "5", "6", "7", "10", "11", "12"]
        palos = ["\u2660", "\u2663", "\u2665", "\u2666"]
        self.cartas = []
        for i in valor:  # creamos el mazo de cartas
            for j in palos:
                carta = Carta(i, j)
                self.cartas.append(carta)

    def mostrar_cartas(self):
        for elemento in self.cartas:
            print(elemento)

    def barajar_carta(self):
        cartas = self.cartas
        random.shuffle(cartas)

    def mostrar_siguiente_carta_y_eliminar_una(self):
        carta = self.cartas
        cantidad = len(self.cartas)
        if cantidad >= 0:
            for elemento in carta:
                self.cartas.remove(elemento)
                cantidad -= 1
                return elemento
        else:
            return "No hay mas cartas para mostar"

    def mostrar_cantidad_de_cartas_restantes(self):
        print("Quedan:", len(self.cartas), "cartas en el mazo")

    def mostrar_cantidad_de_cartas_solicitadas(self, cartasSolicitadas):
        mazo = self.cartas
        int(cartasSolicitadas)
        cantidadDeCartasDisponibles = len(self.cartas)
        if cantidadDeCartasDisponibles >= cartasSolicitadas:
            for elemento in range(cartasSolicitadas):
                print(mazo[elemento])
        else:
            print("No quedan cartas disponibles")


# main
mazo = Baraja()  # creamos el mazo
mazo.barajar_carta()  # barajamos

# pruebas
mazo.mostrar_cantidad_de_cartas_restantes()

mazo.mostrar_siguiente_carta_y_eliminar_una()

mazo.mostrar_siguiente_carta_y_eliminar_una()

mazo.mostrar_cantidad_de_cartas_restantes()

mazo.mostrar_cantidad_de_cartas_solicitadas(3)
