import random


class Carta:
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


class Baraja:
    def __init__(self):
        self.cartas = []

    def crear_baraja(self):
        valor = ["1", "2", "3", "4", "5", "6", "7", "10", "11", "12"]
        palos = ["ORO", "ESPADAS", "COPAS", "BASTOS"]
        for i in valor:
            for j in palos:
                carta = Carta(i, j)
                self.cartas.append(carta)

    def sacar_carta(self):
        posicionCarta = self.cartas[0]
        print(posicionCarta)
        return self.cartas.pop(0)

    def mostrar_cartas(self):
        for elemento in self.cartas:
            print(elemento)

    def mezclar_cartas(self):
        random.shuffle(self.cartas)

    def reiniciar_cartas(self):
        self.cartas.clear()
        self.crear_baraja()


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

    def tomar_carta(self, mazo):
        return mazo.sacar_carta()

    def __str__(self):
        return "{}".format(self.nombre)


class Juego:
    def __init__(self,mazo):
        self.jugadores = []
        self.mazo = mazo

    def iniciar_juego(self):
        bol=False
        contador=0
        nombre=0

        cantidadJugadores = 2#int(input("ingrese cantidad de jugadores"))

        for elemento in range(cantidadJugadores):
            jugador = Jugador()
            self.jugadores.append(jugador)

        self.mazo.crear_baraja()
        self.mazo.mezclar_cartas()
        #contador=len(self.mazo)

        while bol != True :
            elemento=0
            while elemento != 5:
                print(elemento)
                carta = self.jugadores[elemento-1].tomar_carta(self.mazo)
                bol = carta.es_uno_de_oro()
                nombre = (self.jugadores[elemento])
                elemento=+1
                if bol == True:
                    elemento=5
        print(nombre)

    def finalizar_juego(self):
        pass

    def get_ganador(self):
        pass

    def eliminar_jugador(self):
        pass

#carta = Carta("1","ORO")
#print(carta.es_uno_de_oro())

mazo = Baraja()
#mazo.crear_baraja()
#mazo.mezclar_cartas()
#mazo.mostrar_cartas()

#jugador = Jugador("pedro")
#jugador.tomar_carta(mazo)
#jugador.tomar_carta(mazo)

juego = Juego(mazo)
juego.iniciar_juego()