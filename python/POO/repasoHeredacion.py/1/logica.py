class Moto():
    def __init__(self, tipoRepuesto):
        self.valorRepuesto = 0
        self.tarifa = 50
        self.tipoRepuesto = tipoRepuesto
        
    def calculoRepuestos(self):
        if self.tipoRepuesto == 1:
            self.valorRepuesto = 150
        elif self.tipoRepuesto == 2:
            self.valorRepuesto = 100
        elif self.tipoRepuesto == 3:
            self.valorRepuesto = 50

    def costoBase(self):
        self.sumaAtributos = self.valorRepuesto + self.tarifa
        self.iva = self.sumaAtributos * 1.19
        return self.iva