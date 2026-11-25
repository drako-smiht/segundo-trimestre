from emple import Empleado

class asesor(Empleado):
    def __init__(self, celular, nombre, apellido, telefono):
        super().__init__(celular, nombre)
        self.apellido = apellido
        self.telefono = telefono