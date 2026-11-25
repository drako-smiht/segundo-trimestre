listaPrecio=[]
class Person:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
        
       
    def comparacion(self):
        if self.precio>1 and self.precio<1000:
            if self.nombre=="susana":
                self.aumentoPrecio=self.precio*1.20
                
            elif self.nombre=="jessica":
                self.aumentoPrecio=self.precio*1.15
                

            elif self.nombre=="wilson":
                self.aumentoPrecio=self.precio*1.10

            else:
                self.aumentoPrecio=self.precio

            listaPrecio.append(self.aumentoPrecio)
        else:
            print("numero muy menor o muy mayor ")
            pass
    def calculo(self):
        self.promedio=sum(listaPrecio)/len(listaPrecio)
        self.total=sum(listaPrecio)
        self.mayor=max(listaPrecio)
        self.menor=min(listaPrecio)

        print(f"El promedio de precios es de:{self.promedio}\n \
        El total de los precios es:{self.total}\n\
        El precio mayor:{self.mayor}\n\
        El precio menor:{self.menor}") 
