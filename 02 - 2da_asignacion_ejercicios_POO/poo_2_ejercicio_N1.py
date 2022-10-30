class TableroDeBasquet: #clase tablero

    def __init__(self, local, visitante, puntos_local=0, puntos_visitantes=0):
        self.local = local
        self.visitante = visitante
        self.puntos_local = puntos_local
        self.puntos_visitantes = puntos_visitantes

    def puntosDeDos_visitantes(self):
        self.puntos_visitantes += 2

    def puntosDeaDos_local(self):
        self.puntos_local += 2

    def puntosDeTres_visitantes(self):
        self.puntos_visitantes += 3

    def puntosDeTres_local(self):
        self.puntos_local += 3

    def puntosDeaUno_local(self):
        self.puntos_local += 1

    def puntosDeaUno_visitante(self):
        self.puntos_visitantes += 1

    def get_puntos_local(self):
        return self.puntos_local

    def get_puntos_visitantes(self):
        return self.puntos_visitantes

    def __str__(self):
        return "El equipo local: {} lleva {} puntos, El equipo visitante: {} lleva {} puntos".format(self.local,
                                                                                                     self.get_puntos_local(),
                                                                                                     self.visitante,
                                                                                                     self.get_puntos_visitantes())


tablero = TableroDeBasquet(local="Argentina", visitante="Brasil")
tablero.puntosDeTres_local()
print(tablero)
