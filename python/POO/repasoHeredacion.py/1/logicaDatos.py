from logica import Moto

class MotoEsp(Moto):

    def __init__(self, nombre, marca, cilindraje, tipoRepuesto):
     
        super().__init__(tipoRepuesto)
        self.nombre = nombre
        self.marca = marca
        self.cilindraje = cilindraje
        self.descuento = 0
        self.total = 0

    def descue(self):
        
        self.calculoRepuestos()
        
       
        base = self.costoBase()

        if self.cilindraje <= 150:
            self.descuento = base * 0.10
        else:
            self.descuento = 0
            
        self.total = base - self.descuento

    def impresion(self):
       
        self.descue()
        
        print(f"\nValor total del repuesto usado: {self.valorRepuesto}\
              \nValor de la tarifa: {self.tarifa}\
              \nValor a pagar sin descuento: {self.sumaAtributos}\
              \nValor total a pagar con descuento: {self.total}")