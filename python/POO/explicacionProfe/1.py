class Person:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def saludar(self):
        print(f"hola,soy:{self.nombre}\n\
              mi edad es:{self.edad}")

nom=input("Digita el nombre:")
edad=int(input("edad:"))
persona1 = Person(nom,edad)
persona1.saludar()
