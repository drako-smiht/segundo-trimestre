listaSueldo = []

class Sueldos:
    def __init__(self, sueldo):
        self.sueldo = sueldo 
        listaSueldo.append(sueldo)
        
    def calculos(self):
       
        self.promedio = sum(listaSueldo) / len(listaSueldo)
        self.mayor = max(listaSueldo)
        self.menor = min(listaSueldo)
        
        print(f"El sueldo mayor fue: {self.mayor}\n\
                El sueldo menor fue: {self.menor}\n\
                El promedio es de: {self.promedio}")
                
        if self.promedio >= 1 and self.promedio <= 4000000:
            print("Sueldo basico")
        elif self.promedio > 4000000 and self.promedio <= 10000000:
            print("Sueldo medio")
        elif self.promedio > 10000000 and self.promedio <= 20000000:
            print("Sueldo alto")
        else:
            print("Error: Sueldo fuera de rango")
    
      
    
