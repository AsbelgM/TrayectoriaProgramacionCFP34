'''Crear una clase Rectángulo que tenga
Los atributos base y altura.
Crear el constructor de la clase que reciba por argumento los valores de la base y la altura.
Los métodos necesarios para:
Calcular el área. La fórmula es base*altura
El perímetro. La formula es 2*base + 2*altura'''


class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        perimetro = (2*self.base) + (2*self.altura)
        return perimetro

    def get_perimetro(self):
        return self.perimetro()

    def area (self):
        area = self.base * self.altura
        return area

    def get_area (self):
        return self.area()

    def __str__(self):
        return "El area es: {} El perimetro es {}".format(self.area(),self.perimetro())






