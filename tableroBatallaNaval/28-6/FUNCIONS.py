import random
def crear_espacio_oceano(numeroIngresado):
    # CREAMOS EL CAMPO O AGUA DEL TALBERO Y LOS NUMEROS DE LA COLUMNA LATERAL
    for k in range(numeroIngresado):
        oceano=[]
        espacio=[]
        for j in range(numeroIngresado):
            espacio.append(0)
            oceano.append(espacio)
    return oceano

# FUNCION NUEVA
def crear_letras_superiores_oceano(numeroIngresado):
    # DECLARAMOS LAS LISTAS VACIAS PARA LUEGO ALMACENAR LOS DATOS QUE SE VAN CREANDO
    oceano = []
    # EL ALFABETO ASCCI CREARA LAS LETRAS DE LA PARTE SUPERIOR
    alfabeto = list(map(chr, range(64, 91)))
    for i in range(numeroIngresado):
        letrasSuperiores = (alfabeto[i + 1])
        # ALMACENAMOS EN UNA LISTA QUE PARA LUEGO MOSTRAR LA PARTE SUPERIOR DEL TABLERO
        oceano.append(letrasSuperiores)
    print("")
    return oceano


# PRE: se debe ingresar un numero entre 1 y 26 (letras de la A ala Z), esto para que sea cuadrado el oceano
# POST: retorna un oceano de juego, la cual seria una matriz cuadrada
def crear_oceano(numeroIngresado):
    # DECLARAMOS LAS LISTAS VACIAS PARA LUEGO ALMACENAR LOS DATOS QUE SE VAN CREANDO
    oceano = []
    letrasDelOceano = []

    # EL ALFABETO ASCCI CREARA LAS LETRAS DE LA PARTE SUPERIOR
    alfabeto = list(map(chr, range(64, 91)))
    for i in range(numeroIngresado):
        print("\t", alfabeto[i + 1], end="")
        letrasDelOceano.append(alfabeto[i + 1])

    # ALMACENAMOS EN UNA LISTA QUE PARA LUEGO MOSTRAR LA PARTE SUPERIOR DEL TABLERO
    oceano.append(letrasDelOceano)
    print("")

    # CREAMOS EL CAMPO O AGUA DEL TALBERO Y LOS NUMEROS DE LA COLUMNA LATERAL

    for k in range(numeroIngresado):
        espacioDelOceano = []
        print(k + 1, end="")
        for j in range(numeroIngresado):
            print("\t", 0, end="")

            # GUARDAMOS EN UNA LISTA EL MAR O CAMPO DE BATALLA

            espacioDelOceano.append(str(0))
        oceano.append(espacioDelOceano)
        print("              ")
    return oceano


# PRE: como parametro pasamos una lista de listas
# POST:devuelve la lista de listas una debajo de la otra
def convertir_oceano_en_lista(oceano, numeroingresadoporelusuario):
    for x in range(numeroingresadoporelusuario + 1):
        if (x + 1 > 1):
            print(x, "\t", *oceano[x])
        else:
            print("\t", *oceano[x])
        x = x + 1


# PRE:el oceano debe ser una lista de listas, debe tener como elementos dentro de la lista "0" o numeros mayores a "0"
# POST:devuelve la listas de listas sustituyendo "0" por "X" o "~" dependiendo si la posicion econtramos "0" o un numero mayor
def disparar_al_oceano(oceano, fila, columna):
    if oceano[fila][columna] != "0":
        oceano[fila][columna] = "X"
    else:
        oceano[fila][columna] = "~"
        return oceano


# PRE:recibe una letra como parametro de la "A" a la "Z", en mayuscula o minuscula
# POST:transforma la letra a mayuscula, devueve el valor que representa esa letra en el codigo ASCII, pero entre el 1 y el 26 (letras del abecedario)
def convertir_letra_a_numero(letraDeColumna):
    letra = ord(letraDeColumna.upper())
    letra = letra - 65
    return letra


# PRE:recibe un barco el cual es una lista con n elementos y el oceano como una lista de listas
# POST:ubica de forma aleatoria el barco dentro del oceano
def ubicar_barcos_en_oceano(barco, oceano):
    i = 0
    numeroAleatorioDeListas = random.randrange(1, 10)
    espacioOcupadoPorElBarco = (len(oceano[0])) + 1 - len(barco)
    numeroAleatorioParaElBarco = (random.randrange(0, espacioOcupadoPorElBarco))
    for i in range(len(barco)):
        if oceano[numeroAleatorioDeListas][(numeroAleatorioParaElBarco)] != 0:
            oceano[numeroAleatorioDeListas][(numeroAleatorioParaElBarco + i)] = barco[i]
            i = i + 1
        else:
            oceano[numeroAleatorioDeListas + 1][(numeroAleatorioParaElBarco + i)] = barco[i]
            i = i + 1
    return oceano
