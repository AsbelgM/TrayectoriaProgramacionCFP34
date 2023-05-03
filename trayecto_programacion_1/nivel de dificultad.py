###IMPORT
import random
###DEF

def solicitar_nivel_de_dificultad():
    dificultad = int(input("1: NIVEL FACIL, 2:NIVEL INTERMEDIO, 3:NIVEL EXPERTO: "))
    while dificultad != 1 and dificultad != 2 and dificultad != 3:
        print("ingrese un nivel de dificultad valido")
        dificultad = int(input("1: NIVEL FACIL, 2:NIVEL INTERMEDIO, 3:NIVEL EXPERTO: "))
    return(dificultad)

def numeros_aleatorio (cantidadDeNumerosDeJuego):
    if cantidadDeNumerosDeJuego == 1:
        numerosTotal = int(10)
    if cantidadDeNumerosDeJuego == 2:
        numerosTotal = int(100)
    if cantidadDeNumerosDeJuego == 3:
        numerosTotal = int(1000)
    return(numerosTotal)


def crear_cantidad_de_intentos (cantidadDeIntentosSegunDif):
    if cantidadDeIntentosSegunDif == 1:
        intentos = int(3)
    if cantidadDeIntentosSegunDif == 2:
        intentos = int(30)
    if cantidadDeIntentosSegunDif == 3:
        intentos = int(300)
    return(intentos)


###MAIN
nivelDeDifi = solicitar_nivel_de_dificultad()
numeroAleatorio = random.randrange(1,numeros_aleatorio(nivelDeDifi))
numeroIngresado = int(input("Ingrese un numero: "))
print(numeroAleatorio)
while numeroIngresado != numeroAleatorio:
    if numeroIngresado < numeroAleatorio:
        print("el numero ingresado es menor")
        numeroIngresado = int(input("Ingrese un numero para adivinar el numero secreto: "))
    else:
        print("el numero ingresado es mayor")
        numeroIngresado = int(input("Ingrese un numero para adivinar el numero secreto: "))
print("EXCELENTE diste con el numero secreto")
