def crear_letras_superiores_del_oceano(numeroQueDeterminaTablero):
    letrasSuperioresDelOceano = []
    alfabeto = list(map(chr, range(65, 91)))
    for i in range (numeroQueDeterminaTablero):
        letras = alfabeto[i]
        i=i+1
        letrasSuperioresDelOceano.append(letras)
    return letrasSuperioresDelOceano

def crear_campo_del_oceano_numeros_laterales(numeroQueDeterminaTablero):
    for k in range(numeroQueDeterminaTablero):
        espacioDelOceano = []
        campo = (k+1)
        espacioDelOceano.append(campo)
        return espacioDelOceano


print(crear_campo_del_oceano_numeros_laterales(2))


