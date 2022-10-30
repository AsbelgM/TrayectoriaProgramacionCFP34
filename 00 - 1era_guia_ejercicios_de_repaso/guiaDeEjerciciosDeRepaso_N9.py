# Def
def calcular_totales(presupuesto):  # pre: una lista que contenga diccionarios
    montos = []  # lista vacia para agregar los montos de los presupuestos
    listaSuma = 0
    for elementos in presupuesto:
        montos.append(elementos["budget"])
        listaSuma = sum(montos)  # sumamos la lista
    return (listaSuma)


# Main
# Variables
presupuesto_uno = ([
    {"name": "John", "age": 21, "budget": 23000},
    {"name": "Steve", "age": 32, "budget": 40000},
    {"name": "Martin", "age": 16, "budget": 2700}
])
presupuesto_dos = ([
    {"name": "John", "age": 21, "budget": 29000},
    {"name": "Steve", "age": 32, "budget": 32000},
    {"name": "Martin", "age": 16, "budget": 1600}
])
