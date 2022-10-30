# Def
# Verifico si existen elementos repetidos en la lista
def verificar_si_existe_elemento_repetido(lista):
    for i in lista:
        elemento = lista.count(i)
        if elemento > 1:
            return True
        return False


# si existen elementos repetidos en la lista se agrupan y mostramos una nueva lista con los elementos en plural
def agrupar_elementos_y_mostrar(lista, existeElementoRepetido):
    elementoRepetido = 0
    if existeElementoRepetido == True:
        for i in lista:
            cantidadDeVecesEnLista = lista.count(i)
            if cantidadDeVecesEnLista > 1:
                elementoRepetido = lista.index(i)
                lista.remove(i)
        lista[elementoRepetido] = lista[elementoRepetido] + str("s")
    return (lista)


# funcion general que verifica si existen elementos repetidos en la lista los agrupa y como ultimo paso devuelve un SET de las listas originales
def lista_resultado(lista):
    existenElementosRepetidos = verificar_si_existe_elemento_repetido(lista)
    if existenElementosRepetidos == True:
        listaDeElementosAgrupados = agrupar_elementos_y_mostrar(lista, existenElementosRepetidos)
        listaConvertidaEnSET = set(listaDeElementosAgrupados)
        return listaConvertidaEnSET
    else:
        listaConvertidaEnSET = set(lista)
        return listaConvertidaEnSET


# Main
# variables
lista1 = ["cow", "pig", "cow", "cow"]
lista2 = ["table", "table", "table"]
lista3 = ["chair", "pencil", "arm"]

# utilizamos las funciones creadas para mostrar
# se debe probar con las las listas (lista1, lista2, lista3)

# en este caso probamos con la lista2
print(lista_resultado(lista1))
