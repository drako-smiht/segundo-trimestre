from claseSueldos import Sueldos

t = "si"
while t == "si":
    sueldo = float(input("Digite su sueldo: "))
    objetoSueldo = Sueldos(sueldo)
    
    t = input("Desea continuar (si|no): ").lower() 

objetoSueldo.calculos()


print("Resumen de atributos guardados:")
print(objetoSueldo.promedio, objetoSueldo.mayor, objetoSueldo.menor)