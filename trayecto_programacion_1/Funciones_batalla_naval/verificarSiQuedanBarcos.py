import funciones_batalla_naval as oceano
tablero = oceano.crear_espacio_oceano(10)

tablero[0][1]="5"
tablero[0][2]="3"
tablero[0][3]="2"
tablero[0][4]="5"
tablero[2][3]="4"

oceano.imprimir_oceano_de_juego(tablero)

#PRE:
#POST:
def devolver_barcos_hundidos(tableroVisible):
    barcosHundidos = []
    listaDeBarcosHundidos = []
    for elemento in tableroVisible:
        if "2" in elemento:
            barcosHundidos.append("2")
        if "3" in elemento:
            barcosHundidos.append("3")
        if "4" in elemento:
            barcosHundidos.append("4")
        if "5" in elemento:
            barcosHundidos.append("5")
    if "2" not in barcosHundidos:
        listaDeBarcosHundidos.append("2")
    if "3" not in barcosHundidos:
        listaDeBarcosHundidos.append("3")
    if "4" not in barcosHundidos:
        listaDeBarcosHundidos.append("4")
    if "5" not in barcosHundidos:
        listaDeBarcosHundidos.append("5")
    if len(listaDeBarcosHundidos) > 0:
        print ("Has hundido los barcos que ocupan: ",listaDeBarcosHundidos ,"posiciones")
    else:
        print("No has hundido ningun barco")


devolver_barcos_hundidos(tablero)