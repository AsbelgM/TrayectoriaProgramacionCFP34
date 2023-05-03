'''def crear_oceano(numeroIngresado):
    # CREAMOS EL CAMPO O AGUA DEL TALBERO Y LOS NUMEROS DE LA COLUMNA LATERAL
    for k in range(numeroIngresado):
        oceano=[]
        espacio=[]
        for j in range(numeroIngresado):
            espacio.append(0)
            oceano.append(espacio)
    return oceano
print(crear_oceano(10))'''
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
    oceano.append("\t")
    alfabeto = list(map(chr, range(64, 91)))
    for i in range(numeroIngresado):
        letrasSuperiores = (alfabeto[i + 1])
        # ALMACENAMOS EN UNA LISTA QUE PARA LUEGO MOSTRAR LA PARTE SUPERIOR DEL TABLERO
        oceano.append(letrasSuperiores)
    print("")
    return oceano

def convertir_oceano_en_lista(oceano, numeroingresadoporelusuario):
    for x in range(numeroingresadoporelusuario):
        print(x+1, "\t", *oceano[x])
        x = x + 1
oceano=crear_espacio_oceano(15)
#convertir_oceano_en_lista(oceano,10)

print(*crear_letras_superiores_oceano(15))
convertir_oceano_en_lista(oceano,15)