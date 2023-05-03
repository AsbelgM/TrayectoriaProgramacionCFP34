###IMPORT
import time
###VARIABLES
n=0
###FUNCIONES

###MAIN
#########SOLICITO AL USUARIO LA CONTRASEÑA
contrasena=int(input("Ingrese su contraseña"))
########PARTE 3 AGREGAR RETRASOS
while contrasena != 1234:
########AGREGO 2 SEGUNDOS DE ESPERA POR CADA RESPUESTA EQUIVOCADA
    n=n+1
    print("piense mejor su respuesta")
    time.sleep(n+2)
    contrasena = int(input("Ingrese su contraseña"))
print("Bienvenido nuevamente")

#######PARTE 4(d) FUNCION QUE RETORNA VALOR BOLEANO TRUE O FALSE
contrasena_buleana=0
def valor_buleanos():
    if contrasena == 1234:
        contrasena_buleana=print(contrasena == 1234)
    else:
        contrasena_buleana=print(contrasena==1234)
    return(contrasena_buleana)
print(valor_buleanos())

manejo_de_contrasena_b