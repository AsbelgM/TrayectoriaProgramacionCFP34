numero= int(input("ingrese un numero"))
def multiplicar(numero):
    n=0
    while n<11:
        n=n+1
        return (str(n) + str(" x ") + str(numero) + str(" = ") + str(n * numero))

print(multiplicar(numero))