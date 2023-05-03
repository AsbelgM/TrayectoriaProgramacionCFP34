# import
import funciones_batalla_naval as oceano

# Def

# Main
# variables
destructor = ["3", "3", "3"]
fragata = ["2", "2"]
portaAviones = ["5", "5", "5", "5", "5"]
acorazado = ["4", "4", "4", "4"]
print("---BIENVENIDO AL JUEGO DE BATALLA NAVAL----")

numeroIngresado = oceano.retornar_nivel_dificultad() #se asigna el nivel de dificultad segun lo que elija el usuario

while numeroIngresado == 1:
    oceano.mostrar_intrucciones()
    numeroIngresado = oceano.retornar_nivel_dificultad() #volvemos al menu inicial para solicitar nivel de jueo

print("\t")
print("\t", " TABLERO DE BATALLA")
letrasSuperiores = oceano.crear_letras_superiores_oceano(numeroIngresado) # creamos el oceano (letras superiores y espacio de juego)
tableroUsuario = oceano.crear_espacio_oceano(numeroIngresado)

tableroOculto = oceano.crear_espacio_oceano(numeroIngresado) # creo un tablero para ubicar los barcos sin que sean visibles

oceano.ubicar_barcos_de_dos_y_tres_posiciones(destructor, fragata, tableroOculto) # asignamos los barcos al tablero oculto
oceano.ubicar_barcos_de_cuatro_y_cinco_posiciones(portaAviones, acorazado, tableroOculto)
print(*letrasSuperiores)
oceano.imprimir_oceano_de_juego(tableroUsuario)
print("\t")
print("Tablero solo lo ve el programador para visualizar los barcos")
print("\t")
print(*letrasSuperiores)
oceano.imprimir_oceano_de_juego(tableroOculto) # mostramos oceano con barcos (SOLO PARA QUE EL PROGRAMADOR VERIFIQUE)

verificarBarcosEnOceano = oceano.verificar_barcos(tableroOculto) # verificamos si el oceano tiene barcos si es asi luego ingrese al ciclo while

#ingresamos al ciclo solicitaremos barcos hasta que no existen mas barcos en el oceano o se acaben la cantidad de intentos
print("tenes 20 intentos para acertar todos los barcos del mapa")
print("El juego ha comenzado ")
numeroIntentos = 20
while verificarBarcosEnOceano == True and numeroIntentos != 0:
    print("")
    letracolumna = str(input("ingrese una letra: "))     # solicitar datos de entrada para columna
    columna = oceano.convertir_letra_a_numero(letracolumna)   # convertimos la letra a un numero

    numeroFila = int(input("ingrese un numero: ")) #dato de entrada para fila

    oceano.disparar_al_oceano(tableroOculto, numeroFila, columna) # actualizar oceano con diparos efectuados

    verificarBarcosEnOceano = oceano.verificar_barcos(tableroOculto) # asigno el nuevo mapa creado y verifico si quedan barcos

    x = int(numeroFila) - 1 #actualizamos el tablero que visualiza el usario para que sean visibles los disparos
    if tableroOculto[x][columna] != "0":
        tableroUsuario[x][columna] = tableroOculto[x][columna]
        tableroOculto[x][columna] = "x"

    numeroIntentos = numeroIntentos - 1  # cantidad de intentos
    print("te restan", numeroIntentos, "intentos")
    print("")

    print(*letrasSuperiores)     # mostramos el oceano con los disparos efectuados
    oceano.imprimir_oceano_de_juego(tableroUsuario)
    oceano.devolver_barcos_hundidos(tableroOculto)



    if verificarBarcosEnOceano == False: # si ya no quedan barcos se termina el juego
        print("FELICITACIONES GANASTE")
    if verificarBarcosEnOceano == True and numeroIntentos == 0: # si finalizan la cantidad de intentos y aun no descubre los barcos se termina el juego
        print("GAME OVER")
