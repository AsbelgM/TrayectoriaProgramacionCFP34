#Escribir una función que retorne True si cada secuencia consecutiva
# de unos es seguida por una secuencia consecutiva de ceros de la misma longitud

p1 = ("110011100010") #➞ True
p2=("101010110") # ➞ False
p3=("111100001100")# ➞ True
p4=("1100")# ➞ False

def numeros_consecutivos(cadena):
    contadorUno = 0
    contadorCero = 0
    lista= []
    lista2=[]
    x=0
    for i in cadena:
        lista.append(i)
        if i == '1':
            contadorUno = contadorUno + 1
        else:
            contadorCero =contadorCero + 1
    if contadorUno == contadorCero:
        return True
    else:
        return False
print(numeros_consecutivos(p4))

'''def check2(lista):
    n = 0
    if lista:
        inc = 1
        prev = lista[0]
        for bit in lista:
            if bit != prev:
                if inc < 0 and n:
                    break
                inc = -inc
                prev = bit
            n += inc
            if n < 0:
                break
    return n == 0'''





numeros_consecutivos(p4)
