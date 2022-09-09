#Def
#funcion que realiza funiones artimeticas de suma, resta, multiplicacion y division
def operacion_sumar(numeroUno,numeroDos):
    int(numeroUno),int(numeroDos)
    resultadoSuma = numeroUno+numeroDos
    resultadoResta =numeroUno-numeroDos
    resultadoMultiplicacion = numeroUno*numeroDos
    #devuelve un mensaje si existe un "0" en el divisor
    if numeroDos == 0:
        return resultadoSuma,resultadoResta,resultadoMultiplicacion,("No es posible dividir entre 0")
    resultadoDivision = numeroUno//numeroDos
    return resultadoSuma, resultadoResta , resultadoMultiplicacion, resultadoDivision

#Main
#variables
print(operacion_sumar(12,12))