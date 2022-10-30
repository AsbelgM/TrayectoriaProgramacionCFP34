# Def
def verificar_orden(elementoConListas):  # pre: recibe una lista con numeros
    lista = elementoConListas[0]
    listaSegundaPosicion = elementoConListas[1]
    resp = 0
    n = 0
    for elemento in lista:
        if elemento == listaSegundaPosicion[1]:
            for j in lista:
                if j - 1 == listaSegundaPosicion[n]:
                    resp = 1
                    n += 1
            if resp == 1:
                print("la segunda lista es la primer lista “movida” en una posición hacia la derecha")
            return True
        return False


# Main
# varibles
simon_says = ([1, 2], [5, 1])
simon_says_two = ([1, 2], [5, 5])
simon_says_three = ([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])
simon_says_four = ([1, 2, 3, 4, 5], [5, 5, 1, 2, 3])
