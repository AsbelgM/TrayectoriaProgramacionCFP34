'''Crear una clase Lampara que tenga:
Un método que prenda la lámpara
Un método que apague la lámpara
Un método que alterne el prendido y apagado de la lámpara
(por ejemplo: si la lámpara estaba prendida, al ejecutarse el método pasará a estado apagada)
Un método que retorne un string según su estado de prendida o apagada:
Si estaba prendida, el método debe retornar “PRENDIDA”
Si estaba apagada, el método debe retornar “APAGADA”
IMPORTANTE: analizar qué atributo debería tener nuestra clase, para poder implementar las funcionalidades solicitadas.
'''


class Lampara:
    def __init__(self, estado=False):  # lampara encendida = True
        self.estado = estado

    def prender(self):
        self.estado = True

    def get_esta_prendida(self):
        return self.estado

    def apagar(self):
        self.estado = False

    def alternar(self):
        self.estado = not(self.estado)


    def get_esta_prendida_str(self):
        if self.estado:
            return str("APAGADA")
        else:
            return str("PRENDIDA")
