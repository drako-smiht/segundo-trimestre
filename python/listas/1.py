edadMayor=[]
edadMenor=[]

totalMenores=0
for x in range(1,11):
    edad=int(input("Digita tu edad:"))
    if edad>1 and edad<50:
        if edad>=18:
            edadMayor.append(edad)
        
        else:
            edadMenor.append(edad)
    else:
        print("No se conto, mayor que 50")
sumaMayores=sum(edadMayor)
sumaMenores=sum(edadMenor)
promedio=(sumaMayores+sumaMenores)/10
totalMenores=len(edadMenor)
totalMayores=len(edadMayor)
mayor=max(edadMayor)
menor=min(edadMenor)
print(f"promedio:{promedio}\
      mayor:{mayor}\
      menor:{menor}\
      Total Mayores:{totalMayores}\
      Total menores:{totalMenores}")

print("-------listas-----")
print(f"lista mayores:{edadMayor}\n listas menores:{edadMenor}")