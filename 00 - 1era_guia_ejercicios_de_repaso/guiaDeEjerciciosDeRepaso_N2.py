''' 2.	Escribir una función que retorne True si cada secuencia consecutiva de unos
 es seguida por una secuencia consecutiva de ceros de la misma longitud'''
# Import
# Def
def numeros_consecutivos(secuenciaConsecutiva):  # pre: recibe una cadena de string con 0s y 1s
    n = 0  # itinerador
    contador = 1
    lista = 1
    for elemento in secuenciaConsecutiva:
        if elemento != lista:  # compara cada elmento con 1
            contador = -contador
            lista = elemento
        n += contador  # Si el elemento es igual a 1 suma, si no resta
    if n == 0:
        return True
    return False


# Main
# variables
secuencia1 = ("110011100010")
secuencia2 = ("101010110")
secuencia3 = ("111100001100")
secuencia4 = ("111")
