# def

class Agenda:  # creamos la clase agenda
    def __init__(self):
        self.contactos = []

    def aniadir_contacto(self, nombre, numero):
        nombre = nombre.upper()
        lista = (nombre, numero)
        self.contactos.append(lista)

    def get_agenda(self):
        print("\tAGENDA TELEFONICA")
        print("NOMBRE\t", "TELEFONO")
        for elemento in self.contactos:
            print(elemento[0], "\t", elemento[1])

    def existe_contacto(self, nombre):
        contador = 0
        nombre = nombre.upper()
        for elemento in self.contactos:
            for i in elemento:
                if i == nombre:
                    contador += 1

        if contador >= 1:
            print("YA EXISTE CONTACTO")
            return True

        print("NO EXISTE CONTACTO")
        return False

    def buscar_contacto(self, nombre):
        nombre = nombre.upper()
        for elemento in self.contactos:
            for i in elemento:
                if i == nombre:
                    print("El numero de telefono de", i, "es:", elemento[1])

    def eliminar_contacto(self, nombre):
        nombre = nombre.upper()
        existeContacto = True
        for elemento in self.contactos:
            for i in elemento:
                if i == nombre:
                    print("se ha eliminado a: ", i, "de la agenda")
                    self.contactos.remove(elemento)
                    existeContacto = False
        if existeContacto == True:
            print("No existe el contacto que desea eliminar")

    def verificar_si_esta_agenda_llena(self):
        cantidadDeContactos = len(self.contactos) + 1
        if cantidadDeContactos > 10:
            print("!ERROR¡ La agenda esta llena")
        print("La agenda NO esta llena")

    def cupos_disponibles(self):
        cantidadDeContactos = len(self.contactos)
        print("Quedan:", 10 - cantidadDeContactos, "cupos disponibles en la agenda")


# main
agenda = Agenda()
