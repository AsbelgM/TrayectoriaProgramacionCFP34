# def
class Instrumento:  # Atributos generales de un instrumento
    pass

    def __init__(self, precio, marca, modelo):
        self.precio = precio
        self.marca = marca
        self.modelo = modelo

    def tocar(self):
        pass

    def __str__(self):
        return "El precio es :{}. la marca es: {}. el modelo es: {}".format(self.precio, self.marca, self.modelo)


class Guitarra(Instrumento):  # heredamos de la clase padre (Instrumento)
    def tocar(self):
        print("Tocando musica de Guitarra")


class Bateria(Instrumento):
    def tocar(self):
        print("Sonando com una Batria")


class Piano(Instrumento):
    def tocar(self):
        print("Tocando musica de Piano")


# Main
guitarra = Guitarra(precio=1500, marca="nickson", modelo="gt2000")  # prueba
print(guitarra)
guitarra.tocar()
