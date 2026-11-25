listaNotas=[]
class Estudiante:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        listaNotas.append(nota)
    def calculos(self):
        self.promedio=sum(listaNotas)/len(listaNotas)

    def decision(self):
        print(f"Estudiante-{self.nombre}")

        if self.promedio>5:
            print("Gano la materia")
        else:
            print("perdio la materia")
        print(f"La materia le quedo con:{self.promedio}")
     

        