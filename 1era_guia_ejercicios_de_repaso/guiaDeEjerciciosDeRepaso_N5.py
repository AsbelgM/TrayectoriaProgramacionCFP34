#isDisarium 135 = 1¹ + 3² + 5³ = 1 + 9 + 125 = 135
#Test driven development
#135
#"135" -> 1-0 3-1 5-2 // 1-1 3-2 5-3
# Implementar

def is_disarium(numero):
    numero = str(numero)
    acumulador = 0
    for caracter in numero:
        posicion = numero.index(caracter) + 1
        acumulador += int(caracter) ** posicion
    return numero == str(acumulador)