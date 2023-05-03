# 1. multiplicar dos números sin usar el símbolo de multiplicación
numero_uno = 4
numero_dos = 8
resultado = 0
for numero in range(numero_uno):
    resultado += numero_dos
print(resultado)

# 2.  ingresar nombre y apellido e imprimirlo al reves
nombre = str()
apellido = str()

def imprimir_al_reves(nombre,apellido):
    return apellido+" "+ nombre

print(imprimir_al_reves("pedro","gonzalez"))