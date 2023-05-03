txt = open('practica_lectura.txt','a')  # permisos:  leer (r) append (a) modificar (w) agregar (x)

# print(txt.read()) # lectura del archivo

#print(txt.readline()) # lectura de una linea

#for elemento in txt: # lectura de todas las lineas
#    print(elemento)

#txt.write('agregamos una nueva linea a nuestro archivo') #agregamos una linea a nuestro archivo

#txt.close() #cerrar archivo


x = open('practica_lectura.txt') #lectura del archivo con nueva linea string
print(x.read())

