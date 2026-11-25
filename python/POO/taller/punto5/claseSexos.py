listaNotas=[]

class Person:
    def __init__(self,sex,nota):
        self.sex=sex
        self.nota=nota
    def comparacion(self):
        if self.sex=="f":
            self.nota-=3
            listaNotas.append(self.nota)
        elif self.sex=="m":
            self.nota+=2
            listaNotas.append(self.nota)
        else:
            print("Escoja un sexo correcto")
    ganaron=0
    perdieron=0
    def calculos(self):
        self.promedio=sum(listaNotas)/len(listaNotas)
        self.mayor=max(listaNotas)
        self.menor=min(listaNotas)
        if self.nota<=3:
            self.ganaron=self.ganaron+1
        else:
            self.perdieron=self.perdieron+1
        
        print(f"Promedio de notas:{self.promedio}\n\
            Ganaron:{self.ganaron}\n\
            Perdieron:{self.perdieron}\n\
            Mayor nota:{self.mayor}\n\
            Nota menor:{self.menor}")
        
        


