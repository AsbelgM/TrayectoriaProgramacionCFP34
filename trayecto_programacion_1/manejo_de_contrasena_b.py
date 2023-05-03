###IMPORT

###DEF

###MAIN
#########SOLICITO AL USUARIO LA CONTRASEÑA
contrasena=int(input("Ingrese su contraseña"))
#########PARTE B MAXIMO 3 INTENTOS
n=2
while n!=0 and contrasena != 1234:
    n = n - 1
    print("-ERROR- CONTRASEÑA INCORRECTA, le quedan", n+1,"intentos")
    contrasena = int(input("Ingrese su contraseña"))
if contrasena != 1234:
    print("SE ALCANZO EL MAXIMO DE INTENTOS")
else:
    print("BIENVENIDO DE NUEVO")