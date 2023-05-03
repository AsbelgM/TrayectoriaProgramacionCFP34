numero = int(input("ingrese un numero "))
lista=[]
def valores_aldiez ():
  n=0
  for i in range (numero,10):
    n=n+1
    i=numero+n
    lista.append(i)
  return (lista)
print(valores_aldiez())
