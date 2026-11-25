class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

class Perro(Animal):

    def HacerSonido(self):
  
        return "Guau"

class Gato(Animal):

    def HacerSonido(self):
        return "Miau"


class raza(Animal):
    def __init__(self, nombre, edad, tipo, raza):
        super().__init__(nombre, edad, tipo)
        self.raza=raza    


mi_perro = Perro("Du", 14, "perro","buldog")
mi_gato = Gato("Michi", 2, "gato", "peludo")

print(f"{mi_perro.nombre} hace: {mi_perro.HacerSonido()}")
print(f"{mi_gato.nombre} hace: {mi_gato.HacerSonido()}")


