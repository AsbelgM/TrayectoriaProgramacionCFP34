#######################################VARIABLES
#creamo una lista de 4 valores
lista_numeros=[25,5,-8,-9]
lista_resultado=[]
n1=lista_numeros[1]
n2=lista_numeros[2]
#######################################PP
#craeam una funcion que almacene la el programa
def multiplicar_lista ():
  n=0
#recoro la lista y multiplico el primero elemento por el resto de la lista
  for i in range(3):
    n=n+1
    i=lista_numeros[0]*lista_numeros[n]
#Agrego los valores a una nueva lista que tiene los resultados de la multiplicacion
    lista_resultado.append(i)
#multiplico los numeros de los otras posiciones por cada elmento restante de la lista
  lista_resultado.append(n1*lista_numeros[2])
  lista_resultado.append(n1*lista_numeros[3])
  lista_resultado.append(n2*lista_numeros[3])
#busco el numero mayor de la lista nueva creada
  numeromayor=max(lista_resultado)
  return (numeromayor)
print(multiplicar_lista())