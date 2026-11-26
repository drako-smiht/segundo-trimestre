listaedades = []
listacompra= []
class metodos:
    def __init__(self,edad,compra):
        self.edad = edad
        listaedades.append(edad)
        self.compra = compra
        listacompra.append(compra)
    def edadesmayores (self):
        mayores=[]
        for t in range(listaedades):
            edad=listaedades
            if edad >= 18:
                mayores.append(edad)
        nmayores=len(mayores)
    def edadesmenores (self):
        menores=[]
        for y in range(listaedades):
            edad=listaedades
            if edad <= 17:
                menores.append(edad)
        self.nmenores=len(menores)

    def compramayor (self):
        self.mayorcompra=max(listacompra)

    def compramenor (self):
        self.menorcompra=min(listacompra)

    def edadmayor (self,):
        self.mayor=max(listaedades)

    def edadmenor (self):
        self.menor=min(listaedades)

    def promediocompra (self):
        self.promedio=sum(listacompra)/len(listacompra)

    def comprama (self):
        mayor4 = []
        for e in range(listacompra):
            compra=listacompra
            if compra >=450:
                mayor4.append(compra)
        
    def comprame (self):
        menor4=[]
        for w in range(listacompra):
            compra=listacompra
            if compra <=449:
                menor4.append(compra)
        
    def mostrar (self):
        print(f"el numero de edades mayores es {self.nmayores}")
        print(f"el numero de menores es {self.nmenores}")
        print(f"la compra mayor es de {self.mayorcompra}")
        print(f"la compra menor es de{self.menorcompra}")
        print(f"la edad mayor es de {self.mayor}")
        print(f"la edades menor es de{self.menor}")
        print(f"el promedio de compra es de{self.promedio}")
