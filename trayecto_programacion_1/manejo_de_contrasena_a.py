###IMPORT

###DEF

###MAIN
#########SOLICITO AL USUARIO LA CONTRASEÑA
contrasena=int(input("Ingrese su contraseña"))
######### SI ES DIFERENTE DE LA ELEGIDA LE SIGUE SOLICITANDO
while contrasena != 1234:
    print("-ERROR- CONTRASEÑA INCORRECTA")
    contrasena = int(input("Ingrese su contraseña"))
######### SI ES CORRECTA LE DA LA BIENVENIDA
print("Bienvenido de nuevo")
