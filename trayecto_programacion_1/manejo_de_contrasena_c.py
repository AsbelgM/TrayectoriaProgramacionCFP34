###IMPORT
import time
###FUNCIONES

###MAIN
n=0
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