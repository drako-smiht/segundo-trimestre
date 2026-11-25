from ase import asesor

class Persona(asesor):
    def __init__(self, celular, nombre, apellido, telefono, correo, direccion):
        super().__init__(celular, nombre, apellido, telefono)
        self.correo = correo
        self.direccion = direccion