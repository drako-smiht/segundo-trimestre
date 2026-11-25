promedioPerdidas=0
promedioGanadas=0
totalCantidad=0
totalnotas=0
perdiomas=0
perdiomenos=0
cantidad=0
contituar="si"
while contituar=="si":
    nota=float(input("ingrese la nota (1 a 5): "))
    if nota>5:
        print(" TIene que tener una nota menor de 5")
    if  nota>1 and nota<2.9:
        promedioPerdidas+=nota
        cantidad+=1
        
        perdiomenos+=1
    else:
        promedioGanadas+=nota
        cantidad+=1
        
        perdiomas+=1
    
        
    contituar=str(input("Desea continuar(si o no ):"))
totalCantidad=cantidad
totalnotas=promedioGanadas+promedioPerdidas
total=(totalnotas/totalCantidad)


if total>=3:
    print("Gano la materia")
else:
    print("perdio la materia")

print("Promedio notas:",total)

       


