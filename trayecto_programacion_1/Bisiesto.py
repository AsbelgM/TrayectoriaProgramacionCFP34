#Solicito al usuario un año
ano=int(input("Ingrese un año"))
# el año debe ser divisible por 4
if ano%4==0:
    if ano%100==0:
# si es divisible entre 4 pero a su vez no entre 100 puede ser bis
# si cumple la ultima condicion ser divisble entre 400
        if ano%400==0:
            print("el año",ano," es bisiesto")
        else:
           print("El año",ano," no es bisiesto")
    else:
        print("El año",ano," es bisiesto")
else:
    print("el año",ano, "no es bisiesto")