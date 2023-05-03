class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_salario(self):
        return self.salario

    def set_nombre(self, valorAsignado):
        self.nombre = valorAsignado

    def set_edad(self, valorAsignado):
        self.edad = valorAsignado

    def set_salaio(self, valorAsignado):
        self.salario = valorAsignado

    def plus_salario(self):
        pass


class Comercial(Empleado):
    def __init__(self, nombre, edad, salario, comision):
        Empleado.__init__(self, nombre, edad, salario)
        self.comision = comision

    def get_comision(self):
        return self.comision

    def set_comision(self, valorAsignado):
        self.comision = valorAsignado

    def plus_salario(self):
        if self.edad > 30 and self.comision > 200:
            self.salario += 300

    def __str__(self):
        return "El empleado: {}, tiene: {} años, Posee un salaio de: {} €".format(self.nombre, self.edad, self.salario)


class Repartidor(Empleado):
    def __init__(self, nombre, edad, salario, zona):
        Empleado.__init__(self, nombre, edad, salario)
        self.zona = zona

    def get_zona(self):
        return self.zona

    def set_zona(self, valorAsignado):
        self.zona = valorAsignado

    def plus_salario(self):
        if self.edad < 25 and self.zona == 3:
            self.salario += 300

    def __str__(self):
        return "El empleado: {}, tiene: {} años, Posee un salario de: {} €".format(self.nombre, self.edad, self.salario)


empleado = Comercial(nombre="Pedro", edad=31, salario=300, comision=300)
empleado.plus_salario()
print(empleado)
