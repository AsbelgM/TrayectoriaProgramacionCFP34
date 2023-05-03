###Import
import random

###Def
#1ERA FUNCION DEVUELVE UN NUMERO ALEATORIO
def numero_aleatorio(numeroAle):
    numeroAle=random.randrange(0,numeroAle)
    return numeroAle

#2DA FUNCION INDICA SI ES PAR
def es_par (numeropar):
    if numeropar %2 == 0:
        return True
    return False
#3RA FUNCION TABLA DE MULTIPLICAR
def tabla_de_multiplicar(numeroMultiplicado):
    n=0
    lista=[]
    for i in range (0,11):
        i=str(i) + str(" x ") + str(numeroMultiplicado)+ str(" = ") + str(i*numeroMultiplicado)
        lista.append(i)
    return(lista)

#4TA FUNCION CONVIERTE A BINARIO
def convertir_a_binario (numeroBinario):
        return (format(numeroBinario,"0b"))



###Main
#INPUT QUE ARROJA EL VALOR QUE LLAMARA A LA FUNCION
opcion = int(input("Ingrese una opcion del menu"))
#SOLICITAR NUMERO AL USUARIO EL CUAL SE USARA COMO PARAMETRO EN LAS FUNCIONES
numeroIngresadoPorElUsuario = int(input("Ingrese un numero"))
#MENU DE FUNCIONES
menu = {1:numero_aleatorio,
       2:es_par,
       3:tabla_de_multiplicar,
       4:convertir_a_binario}
#IMPRIMIMOS LA FUNCION
print(menu.get(opcion)(numeroIngresadoPorElUsuario))

