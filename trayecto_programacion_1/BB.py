#Import
import FUNCIONS as oceanoBatalla
import random

#Def

#Main
buque = ["3","3","3"]
titanic=["5","5","5","5","5",]
numeroIngresadoPorElUsuario = int(input("Ingrese un numero para definir la dificultad de juego"))
oceanoCreado = oceanoBatalla.crear_oceano(numeroIngresadoPorElUsuario)
oceanoBatalla.convertir_oceano_en_lista(oceanoCreado,numeroIngresadoPorElUsuario)
oceanoConBarcos = oceanoBatalla.ubicar_barcos_en_oceano(buque,oceanoCreado)
oceanoBatalla.convertir_oceano_en_lista(oceanoConBarcos,numeroIngresadoPorElUsuario)