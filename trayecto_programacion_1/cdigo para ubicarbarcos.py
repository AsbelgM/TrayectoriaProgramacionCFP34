import funciones_batalla_naval as oceano
import random
tableroPrueba = [["0","0","0","0","0","0"], ["0", "0","0", "0","0","0"], ["0", "0","0", "0","0","0"], ["0", "0","0", "0","0","0"], ["0", "0","0", "0","0","0"],["0", "0","0", "0","0","0"]]
buque = ["3", "3", "3"]
bote = ["2", "2"]
oceano.imprimir_oceano_de_juego(tableroPrueba)
def ubicar_barcos_en_horizotal_vertical(barco,oceano):
    espacioOcupadoPorElBarco = (len(oceano[0])) + 1 - len(barco)
    orientacionDeBarco = random.randrange(2)
    numeroAleatorioDeListas = random.randrange(0,espacioOcupadoPorElBarco-1)
    numeroAleatorioParaElBarco = random.randrange(0,espacioOcupadoPorElBarco)
    print(orientacionDeBarco)
    for elemento in oceano:
        for numero in elemento:
            if numero != "0":
                numeroAleatorioDeListas = numeroAleatorioDeListas+1

    i=0
    if orientacionDeBarco == 1:
        for i in range(len(barco)):
            if oceano[numeroAleatorioDeListas+i][(numeroAleatorioParaElBarco)] == "0":
                if oceano[numeroAleatorioDeListas+i][(numeroAleatorioParaElBarco)] == "0":
                    oceano[numeroAleatorioDeListas+i][numeroAleatorioParaElBarco] = barco[i]
                else:
                    oceano[numeroAleatorioDeListas-i][numeroAleatorioParaElBarco] = barco[i]
                i=i+1

    else:
        for i in range(len(barco)):

            if oceano[numeroAleatorioDeListas][(numeroAleatorioParaElBarco+i)] == "0":
                if oceano[numeroAleatorioDeListas][(numeroAleatorioParaElBarco+i)] == "0":
                    oceano[numeroAleatorioDeListas][numeroAleatorioParaElBarco+i] = barco[i]
                else:
                    oceano[numeroAleatorioDeListas][numeroAleatorioParaElBarco-i] = barco[i]
                i=i+1
    return oceano



ubicar_barcos_en_horizotal_vertical(buque,tableroPrueba)
ubicar_barcos_en_horizotal_vertical(bote,tableroPrueba)
oceano.imprimir_oceano_de_juego(tableroPrueba)

def verificar_numero_ingresado():
    print("Bienvenido elija el nivel de dificultad ")
    print("A : facil (tableroOculto  10x10)")
    print("B : intermedio (tableroOculto  20x20)")
    print("C : Dificil (tableroOculto  25x25)")
    dificultad = {'A': 10, 'B': 20, 'C': 25}
    letra = input("Ingrese una letra: ")
    letra = letra.upper()
    valor=(dificultad.get(letra))
    while letra != "A" or "B" or "C":
        print("elija el nivel de dificultad correcto A B o C ")
        numero=input("ingrese una letra : ")
    return valor


verificar_numero_ingresado()





def ubicar_barcos_de_cuatro_y_cinco_espacios(barcoDeCincoEspacios,oceano):
    orientacionDeBarco = 1
    print(orientacionDeBarco)
    n=0
    numeroAleatorioDeListas = 2
    if orientacionDeBarco == 1:
        for i in range(len(barcoDeCincoEspacios)):
            for j in oceano[numeroAleatorioDeListas]:
                if j == 0:
                    oceano[numeroAleatorioDeListas][n] = barcoDeCincoEspacios[n]
                n=n+1
    return oceano