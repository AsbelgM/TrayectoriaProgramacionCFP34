# numeroingresadoporelusuario = int(input("introduzca un numero para definir el tamaño del tablero de juego:"))
print("-----------------parte1-CREAR TABLERO-----------------------------")

# CREAMOS EL TABLERO BASADO EN LA CANTIDAD DE CASILLAS QUE INGRESE EL USUARIO
def crear_oceano(numeroing):
    # DECLARAMOS LAS LISTAS VACIAS PARA LUEGO ALMACENAR LOS DATOS QUE SE VAN CREANDO
    oceano = []
    letrasDelOceano = []

    # EL ALFABETO ASCCI CREARA LAS LETRAS DE LA PARTE SUPERIOR

    alfabeto = list(map(chr, range(64, 91)))
    for i in range(numeroing):
        print("\t", alfabeto[i + 1], end="")
        letrasDelOceano.append(alfabeto[i + 1])

    # ALMACENAMOS EN UNA LISTA QUE LUEGO PARA MOSTRAR LA PARTE SUPERIOR DEL TABLERO

    oceano.append(letrasDelOceano)
    print("")

    # CREAMOS EL CAMPO O AGUA DEL TALBERO Y LOS NUMEROS DE LA COLUMNA LATERAL

    for k in range(numeroing):
        espacioDelOceano = []
        print(k + 1, end="")
        for j in range(numeroing):
            print("\t", 0, end="")

            # GUARDAMOS EN UNA LISTA EL MAR O CAMPO DE BATALLA

            espacioDelOceano.append(str(0))
        oceano.append(espacioDelOceano)
        print("              ")
    return oceano


# FUNCION PARA CONVERTIR EL TABLERO EN LISTAS UNA DEBAJO DE LA OTRA
def convertir_tablero_en_lista(tablero, numeroingresadoporelusuario):
    for x in range(numeroingresadoporelusuario + 1):
        if (x + 1 > 1):
            print(x, "\t", *tablero[x])
        else:
            print("\t", *tablero[x])
        x = x + 1


def disparos_al_oceano(oceano, fila, columna):
    if oceano[fila][columna] != "0":
        oceano[fila][columna] = "X"
    else:
        oceano[fila][columna] = "~"
        return oceano


# FUNCION PARA CONVERTIR LA LETRA INGRESADA A UN NUMERO
def convertir_numero_a_letra(letraDeColumna):
    letra = ord(letraDeColumna.upper())
    letra = letra - 65
    return letra

#UBICAR BARCOS


##pp
columna = input("Ingrese una letra")
fila = int(input("ingrese un numero"))
columna = convertir_numero_a_letra(columna)

oceano = crear_oceano(10)
print("-----------------parte3-MAR CON BARCOS-----------------------------")
oceano = disparos_al_oceano(oceano, fila, columna)

convertir_tablero_en_lista(oceano, 10)
