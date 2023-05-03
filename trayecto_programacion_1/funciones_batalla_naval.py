# import
import random


# PRE: esta funcion imprime un menu de opciones y retorna el valor segun la opcion que escoja el usuario
# POST: la funcion retorna 4 valores (1, 10, 15 o 25) segun la letra que escoja el usuario
def retornar_nivel_dificultad():
    print("Elija el nivel de dificultad ")
    print("A : facil (tablero  10x10)")
    print("B : intermedio (tablero  15x15)")
    print("C : Dificil (tablero  25x25)")
    print("D : ver instrucciones de juego ")
    dificultad = {'A': 10, 'B': 15, 'C': 25, 'D': 1}
    letra = input("Ingrese una letra: ")
    letra = letra.upper()
    opciones = dificultad.keys()
    while letra not in opciones:
        print("elija el nivel de dificultad correcto A B o C ")
        letra = input("ingrese una letra : ")
        letra = letra.upper()
    numero = int((dificultad.get(letra)))
    return numero


# POST: muestra una lista de intrucciones
def mostrar_intrucciones():
    print("\t")
    print("Instrucciones de juego")
    print("1: debes elegir un nivel de dificultad")
    print("2: el juego consta de 4 barcos ubicados aleatoriamente en el mapa")
    print("3: debes efectuar un disparo tomando como guia los numeros de la fila y las letras de cada columna ")
    print("4: el tablero de juego mostrara (x) si impactaste un barco o (~) si impactaste al agua")
    print("5: si logras derribar todos los barcos antes de que se agoten la cantidad de intentos ganas")
    print("\t")


# PRE: se debe ingresar un numero entre 1 y 26 (letras de la A ala Z)
# POST: retorna las letras superiores del oceano de juego
def crear_letras_superiores_oceano(numeroIngresado):
    letrasOceano = []
    letrasOceano.append("\t")
    alfabeto = list(map(chr, range(64, 91)))
    for i in range(numeroIngresado):
        letrasSuperiores = (alfabeto[i + 1])
        # ALMACENAMOS EN UNA LISTA QUE PARA LUEGO MOSTRAR LA PARTE SUPERIOR DEL TABLERO
        letrasOceano.append(letrasSuperiores)
    return letrasOceano


# PRE: se debe ingresar un numero entre 1 y 26 (letras de la A ala Z), esto para que sea cuadrado el oceano
# POST: retorna un oceano de juego, la cual seria una matriz cuadrada
def crear_espacio_oceano(numeroIngresado):
    CampoOceano = []
    for k in range(numeroIngresado):
        espacio = []
        for j in range(numeroIngresado):
            espacio.append("0")
        CampoOceano.append(espacio)
    return CampoOceano


# PRE: como parametro pasamos una lista de listas
# POST:imprime la lista de listas de forma horizontal
def imprimir_oceano_de_juego(oceano):
    cantidadDeCiclos = len(oceano)
    for x in range(cantidadDeCiclos):
        print(x + 1, "\t", *oceano[x])
        x = x + 1


# PRE:recibe una letra como parametro de la "A" a la "Z", en mayuscula o minuscula
# POST:devueve el valor que representa esa letra en el codigo ASCII, y reasgina un numero en orden entre el 1 las 26 letras del abecedario
def convertir_letra_a_numero(letrasDeColumnas):
    letra = ord(letrasDeColumnas.upper())
    letra = letra - 65
    letra = int(letra)
    return letra


# PRE:el oceano debe ser una lista de listas, debe tener como elementos dentro de la lista "0"
# POST:devuelve la listas de listas sustituyendo "0" por "X" o "~" dependiendo de lo que encuentre en la posicion
def disparar_al_oceano(oceano, fila, columna):
    x = int(fila) - 1
    y = int(columna)
    if oceano[x][y] != "0":
        oceano[x][y] = "x"
        print("Tocaste a un barco")
    else:
        oceano[x][y] = "~"
        print("Fallaste")
    return oceano


# ESTA OTRA FUNCION TAMBIEN UBICA BARCOS PARA LA VERSION 2.0
# PRE:recibe un barco el cual es una lista con n elementos y el oceano como una lista de listas
# POST:ubica de forma aleatoria el barco dentro del oceano
def ubicar_barcos_en_oceano(barco, oceano):
    i = 0
    numeroAleatorioDeListas = random.randrange(0, 10)
    espacioOcupadoPorElBarco = (len(oceano[0])) + 1 - len(barco)
    numeroAleatorioParaElBarco = (random.randrange(0, espacioOcupadoPorElBarco))
    for i in range(len(barco)):
        if oceano[numeroAleatorioDeListas][(numeroAleatorioParaElBarco)] != "0":
            oceano[numeroAleatorioDeListas][(numeroAleatorioParaElBarco + i)] = barco[i]
            i = i + 1
        else:
            oceano[numeroAleatorioDeListas + 1][(numeroAleatorioParaElBarco + i)] = barco[i]
            i = i + 1
    return oceano


# PRE:compara si en cada elemento de una lista de listas, existe algun valor distinto a los incluido en la lista "signos"
# POST:retorna True si existe un elemento distinto, y False si no encuentra algun elemento distinto
def verificar_barcos(oceano):
    signos = ["0", "x", "~"]
    for lista in oceano:
        for elemento in lista:
            if elemento not in signos:
                return True
    return False


# PRE:como parametros necesitamos una lista de listas de mas de 5*5 o mas, y 2 listas que contengan 2 o 3 elementos cada una
# POST:ubica y retorna de forma aleatoria horizontal o vertical las listas de 2 o 3 elementos dentro de la lista principal oceano sin que estas coincidan
def ubicar_barcos_de_cuatro_y_cinco_posiciones(barcoDeCincoEspacios, barcoDeCuatroEspacios, oceano):
    n = 0
    orientacionVerticaloHorizontal = random.randrange(2)
    numeroColumna = random.randrange(2)
    numeroColumnaDos = random.randrange(len(oceano) - len(barcoDeCincoEspacios))
    numeroAleatorioLista = random.randrange(2, len(barcoDeCincoEspacios))
    numeroAleatorioListaDos = random.randrange(2)

    if orientacionVerticaloHorizontal == 1:
        for i in range(len(barcoDeCincoEspacios)):
            oceano[numeroColumna][numeroAleatorioLista + i] = barcoDeCincoEspacios[i]
        for i in range(len(barcoDeCuatroEspacios)):
            oceano[numeroColumnaDos + i][numeroAleatorioListaDos] = barcoDeCuatroEspacios[i]
    if orientacionVerticaloHorizontal == 0:
        for i in range(len(barcoDeCincoEspacios)):
            oceano[numeroColumnaDos + i + 1][numeroAleatorioListaDos] = barcoDeCincoEspacios[i]
        for i in range(len(barcoDeCuatroEspacios)):
            oceano[numeroColumna][numeroAleatorioLista + i] = barcoDeCuatroEspacios[i]
    return oceano


# PRE:como parametros necesitamos una lista de listas de mas de 5*5 o mas, y 2 listas que contengan 4 o 5 elementos cada una
# POST:ubica y retorna de forma aleatoria horizontal o vertical las listas de 4 o 5 elementos dentro de la lista principal oceano sin que estas coincidan
def ubicar_barcos_de_dos_y_tres_posiciones(barcoDeTresEspacios, barcoDeDosEspacios, oceano):
    i = 0
    orientacionVerticaloHorizontal = random.randrange(2)
    numeroAleatorioDeListasVertical = random.randrange(4, len(oceano) - 3)
    numeroAleatorioDeListas = random.randrange(len(oceano) - 3, len(oceano) - 2)
    numeroAleatorioParaElBarco = random.randrange(3, len(oceano) - len(barcoDeTresEspacios))

    if orientacionVerticaloHorizontal == 1:
        for i in range(len(barcoDeTresEspacios)):
            oceano[numeroAleatorioDeListasVertical + i][numeroAleatorioParaElBarco] = barcoDeTresEspacios[i]
            i = i + 1
        for i in range(len(barcoDeDosEspacios)):
            oceano[numeroAleatorioDeListas][numeroAleatorioParaElBarco + i + 2] = barcoDeDosEspacios[i]
            i = i + 1
    if orientacionVerticaloHorizontal == 0:
        for i in range(len(barcoDeDosEspacios)):
            oceano[numeroAleatorioDeListas + i - 4][numeroAleatorioParaElBarco] = barcoDeDosEspacios[i]
        for i in range(len(barcoDeTresEspacios)):
            oceano[numeroAleatorioDeListasVertical + 2][numeroAleatorioParaElBarco + i] = barcoDeTresEspacios[i]
            i = i + 1
    return oceano


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
        print("Has hundido los barcos que ocupan: ", listaDeBarcosHundidos, "posiciones")
    else:
        print("No has Hundido ningun barco")
