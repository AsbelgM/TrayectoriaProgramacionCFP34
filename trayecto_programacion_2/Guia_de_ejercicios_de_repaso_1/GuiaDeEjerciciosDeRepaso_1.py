lista1 = ["cow", "pig", "cow", "cow"]
lista2 = ["table", "table", "table"]
lista3 = ["chair", "pencil", "arm"]

#Verifico si existen elementos repetidos en la lista
def verificar_si_existe_elemento_repetido (lista):
    for i in lista:
        elemento = lista.count(i)
        if elemento > 1:
            return True
        return False

#si existen elementos repetidos en la lista se agrupan y mostramos una nueva lista con los elementos en plural
def agrupar_elementos_y_mostrar(lista,existeElementoRepetido):
    elementoRepetido = 0
    if existeElementoRepetido == True:
        for i in lista:
            cantidadDeVecesEnLista = lista.count(i)
            if cantidadDeVecesEnLista > 1:
                elementoRepetido = lista.index(i)
                lista.remove(i)
        lista[elementoRepetido] = lista[elementoRepetido] + str("s")
    print(lista)

def lista_resultado(lista,listaAgrupada):
    if listaAgrupada == True:
        for i in lista:
            cantidadDeVecesEnLista = lista.count(i)
            if cantidadDeVecesEnLista > 1:
                elementoRepetido = lista.index(i)
                lista.remove(i)
        lista[elementoRepetido] = lista[elementoRepetido] + str("s")



#utilizamos las funciones creadas para mostrar
#se debe probar con las las listas (lista1, lista2, lista3)
#en este caso probamos con la lista que no tiene elementos duplicados
existeElementoRepetido = verificar_si_existe_elemento_repetido(lista3)
agrupar_elementos_y_mostrar(lista3,existeElementoRepetido)

