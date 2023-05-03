femenino = "f"
masculino =  "m"
# SOLICITAMOS AL USUARIO QUE INGRESE SUS AÑOS DE APORTES DEBEN SER MAYOR A 30 PARA CONTINUAR
aportes= int(input("Ingrese sus años de aporte"))
if aportes >= 30:
    edad=int(input("ingrese su edad"))
    if edad<60:
        print("No cumple con la edad para jublarse")
    elif edad<= 65:
        genero = input("Ingrese su genero f:Femenino, m:Masculino")
        if genero == "f":
            print("Se Puede jubilar felicidades señora")
        else:
            print("No se puede jubilar Señor")
    else:
        print("se puede jubilar")
else:
    print("siga laburando")
