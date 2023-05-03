# def
def elevar_numeros_cuadrado(cifra_entrada):
    cifra_entrada = str(cifra_entrada)
    lista = []
    resultado = str()
    for i in cifra_entrada:
        i = int(i)
        i = i ** 2
        lista.append(i)
    for elemento in lista:
        resultado = resultado + str(elemento)
    return (resultado)


# Main
# Variables
lista_de_numeros_uno = (9119)
lista_de_numeros_dos = (2483)
lista_de_numeros_tres = (3212)
