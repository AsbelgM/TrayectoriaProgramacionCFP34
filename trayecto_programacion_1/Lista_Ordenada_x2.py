#CREAMOS LA LISTA QUE ORGANIZAREMOS POR LA 2DA LETRA
lista = ["perro","gato","leon","oso","jirafa","elefante","cocodrilo","mantarayas","ardilla","vaca","tigre"]
#DECLARAMOS UNA LISTA VACIA PARA GUARDAR LA LISTA QUE ORGANIZAREMOS POR LA SEGUNDA LETRA
lista2 =[]
lista3=[]
for x in lista:
#ENVIAMOS AL FINAL LA PRIMERA LETRA DE CADA PALABRA
    x=x[1:]+x[0]
#AGREGAMOS A UNA NUEVA LISTA LOS VALORES CREADOS
    lista2.append(x)
#ORGANIZAMOS LA LISTA POR ORDEN ALFABETICO
    lista2.sort()
#DEVOLVEMOS LA ULTIMA LETRA AL PRINCIPIO DE CADA PALABRA
for j in lista2:
    j=j[-1]+j[0:-1]
    lista3.append(j)
#MOSTRAMOS LA LISTA
print(lista3)
