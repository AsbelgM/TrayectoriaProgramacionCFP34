# Import
import Funci as oceanoBatalla
import random
import
# Def

# Main
buque = ["3", "3", "3"]
titanic = ["5", "5", "5", "5", "5", ]
velero = ["4","4","4","4"]
posicionesDeBarcos = int(14)
#numeroIngresadoPorElUsuario = int(input("Ingrese un numero para definir la dificultad de juego"))
print("---OCEANO CREADO---")
oceanoCreado = oceanoBatalla.crear_oceano(10)
print("---OCEANO LISTA DE LISTAS---")
oceanoBatalla.convertir_oceano_en_lista(oceanoCreado, 10)
print("---OCEANO CON BARCOS---")
oceanoBatalla.ubicar_barcos_en_oceano(buque, oceanoCreado)
oceanoBatalla.ubicar_barcos_en_oceano(titanic, oceanoCreado)
oceanoBatalla.ubicar_barcos_en_oceano(velero,oceanoCreado)
oceanoBatalla.convertir_oceano_en_lista(oceanoCreado, 10)
#JUEGO PRINCIPAL

#while oceano[fila][columna] =!