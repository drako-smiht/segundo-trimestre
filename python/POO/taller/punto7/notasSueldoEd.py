listaNota = []
listaSueldos = []
listaEdad = []

class Persona:
    def __init__(self, sueldos, edades, notas):
        self.sueldos = sueldos
        self.edades = edades
        self.notas = notas
        
        self.gano = 0
        self.perdio = 0
        self.prom = 0
        self.mayor = 0
        self.menor = 0
        self.sueldoMayor = 0
        self.sueldoMenor = 0
        self.promedioSueldo = 0
        self.edadMayor = 0
        self.edadMenor = 0
        self.mayorEdad = 0
        self.menorEdad = 0

        listaNota.append(notas)
        listaSueldos.append(sueldos)
        listaEdad.append(edades)

    def perdioGano(self):
        self.gano = 0
        self.perdio = 0
        for n in listaNota:
            if n < 6:
                self.gano += 1
            else:
                self.perdio += 1

    def promedio(self):
        if len(listaNota) > 0:
            self.prom = sum(listaNota) / len(listaNota)

    def mayorMenor(self):
        self.mayor = 0
        self.menor = 0
        for s in listaSueldos:
            if s > 450:
                self.mayor += 1
            else:
                self.menor += 1

    def mayorMenorSueldo(self):
        if len(listaSueldos) > 0:
            self.sueldoMayor = max(listaSueldos)
            self.sueldoMenor = min(listaSueldos)
            self.promedioSueldo = sum(listaSueldos) / len(listaSueldos)

    def calcularEdades(self):
        if len(listaEdad) > 0:
            self.edadMayor = max(listaEdad)
            self.edadMenor = min(listaEdad)
        
    def mayorMenorEdad(self):
        self.mayorEdad = 0
        self.menorEdad = 0
        for e in listaEdad:
            if e > 18:
                self.mayorEdad += 1
            else:
                self.menorEdad += 1

    def impresion(self):
        self.perdioGano()
        self.promedio()
        self.mayorMenor()
        self.mayorMenorSueldo()
        self.calcularEdades()
        self.mayorMenorEdad()

        print(f"Cuantas notas ganaron:{self.gano}\n"
              f"cuantas notas perdieron:{self.perdio}\n"
              f"promedio notas:{self.prom}\n"
              f"sueldos mayores:{self.mayor}\n"
              f"sueldos menores:{self.menor}\n"
              f"sueldo mayor:{self.sueldoMayor}\n"
              f"sueldo menor:{self.sueldoMenor}\n"
              f"promedio sueldos:{self.promedioSueldo}\n"
              f"edad mayor:{self.edadMayor}\n"
              f"edad menor:{self.edadMenor}\n"
              f"total mayores:{self.mayorEdad}\n"
              f"total menores:{self.menorEdad}")