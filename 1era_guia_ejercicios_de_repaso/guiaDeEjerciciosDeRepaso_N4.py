# def
def existeColorEnPoker(tablero, cartasEnMano):
    existeColor = 0
    lista = []
    for elemento in tablero:
        for i in elemento:
            lista.append(i)
    for j in lista:
        if j == cartasEnMano[1][2]:
            existeColor = existeColor + 1
        if j == cartasEnMano[0][2]:
            existeColor = existeColor + 1
    if existeColor >= 5:
        return True
    return False


# Main
# Variables
tableroUno = ["A_S", "J_H", "7_D", "8_D", "10_D"]
cartasEnManoUno = ["J_D", "3_D"]

tableroDos = ["10_S", "7_S", "9_H", "4_S", "3_S"]
cartasEnManoDos = ["K_S", "Q_S"]

tableroTres = ["3_S", "10_H", "10_D", "10_C", "10_S"]
cartasEnManoTres = ["3_S", "4_D"]

print(existeColorEnPoker(tableroTres, cartasEnManoTres))
