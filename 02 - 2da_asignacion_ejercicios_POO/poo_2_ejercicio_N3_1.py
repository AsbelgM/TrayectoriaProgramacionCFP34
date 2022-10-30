# import
import poo_2_ejercicio_N3_0 as composicion_baraja


# def
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

    def tomar_carta(self, mazo):
        return mazo.sacar_carta()

    def __str__(self):
        return "{}".format(self.nombre)


class Juego:

    def __init__(self, mazo):
        self.jugadores = []
        self.mazo = mazo

    def ingresar_jugadores_participantes(self):
        cantidadJugadores = int(input("ingrese cantidad de jugadores"))

        for elemento in range(cantidadJugadores):
            jugador = Jugador(input("Ingrese el nombre del jugador:"))
            self.jugadores.append(jugador)

    def iniciar_juego(self):
        contador = 0

        self.mazo.crear_baraja()
        self.mazo.mezclar_cartas()

        while len(self.jugadores) != 1:
            carta = self.jugadores[contador].tomar_carta(self.mazo)
            salioElUnoDeOro = carta.es_uno_de_oro()

            if salioElUnoDeOro:
                self.eliminar_jugador(contador)
                self.mazo.crear_baraja()
                self.mazo.mezclar_cartas()
                contador = -1

            elif not salioElUnoDeOro and contador == (len(self.jugadores) - 1):
                contador = -1

            contador += 1

    def get_ganador(self):
        return self.jugadores[0].nombre

    def eliminar_jugador(self, ubicacion):
        del self.jugadores[ubicacion]

#Main
mazo = composicion_baraja.Baraja()
juego = Juego(mazo)

#Pruebas
juego.jugadores = [Jugador("Asbel"), Jugador("Angel"), Jugador("Heydi")]
juego.iniciar_juego()
print(juego.get_ganador())
