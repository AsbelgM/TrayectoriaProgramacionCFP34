

def retornar_nivel_dificultad():
    print("Bienvenido elija el nivel de dificultad ")
    print("A : facil (tableroOculto  10x10)")
    print("B : intermedio (tableroOculto  20x20)")
    print("C : Dificil (tableroOculto  25x25)")
    dificultad = {'A': 10, 'B': 20, 'C': 25}
    letra = input("Ingrese una letra: ")
    letra = letra.upper()
    opciones = dificultad.keys()
    while letra not in opciones :
        print("elija el nivel de dificultad correcto A B o C ")
        letra=input("ingrese una letra : ")
        letra = letra.upper()
    numero=(dificultad.get(letra))
    print(numero)
    return numero


retornar_nivel_dificultad()