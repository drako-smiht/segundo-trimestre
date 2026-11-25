class empleado:
    def __init__(self,nombre,sueldo):
        self.nombre=nombre
        self.sueldo=sueldo
    def impuesto(self,sueldo):
        if sueldo>3000:
            restaSueldo=sueldo*0.20
            total=sueldo-restaSueldo
            self.sueldo=total
        else:
            print("No pagas impuestos")

        
        