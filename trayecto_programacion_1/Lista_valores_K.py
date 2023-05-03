#Generamos la lista con los valores numericos
lista=[10,15,20,30,4,90,25,14,5,3,88,91]

#Solicitamos al usuario que ingrese un valor K entre 1 y 100
k = int(input("Ingrese un valor entero del 1 al 100: "))

#recorremos la lista y buscamos valores menores a k
print("Los valores menores al ingresado son: ")
for i in lista:
    if(k>i):
        print(i)
#Recorremos y buscamos los valores mayores a k
print("los valores mayores al ingresado son: ")
for i in lista:
    if(k<i):
        print(i)
#recorremos y buscamos valores igual al ingresado K
print("Valores iguales al ingresado: ")
for i in lista:
    if (k==i):
        print((i))
#Buscamos los multiplos del valor ingresado K
print("los multiplos del valor son")
for i in lista:
    if(i%k==0):
        print(i)
#FIN DEL PROGRAMA


"perro","gato","araña","leon","oso","delfin","ballena","pez","jirafa","foca","tiburon","pelicano"