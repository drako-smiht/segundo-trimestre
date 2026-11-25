contadorMenor=0
contadorMayor=0
edadMayor=0
edadMenor=0
promedioEdadMenor=0
promedioEdadMayor=0
continuar="si"
while continuar=="si":
    edad=int(input("ingrese la edad:"))
    if edad>=1 and edad<=50:
      if edad>=18:
        contadorMayor+=1
        edadMayor=edad
        if edadMayor>edad:
          edadMayor=edadMayor
        promedioEdadMayor=edadMayor+edad
      else:
       contadorMenor+=1
       edadMenor=edad
       if edadMenor<edad:
         edadMenor=edadMenor
       promedioEdadMenor=edadMenor+edad
    else:
      print("Edad mayor de 50")
    
    continuar=str(input("Desea continuar(si o no):"))
    
promedio=(promedioEdadMayor+promedioEdadMenor)/(contadorMayor+contadorMenor)
print(f"son mayores :{contadorMayor} \
       son menores:{contadorMenor} ")
print(f"La edad mayor fue de:{edadMayor}\
      La edad menor fue de:{edadMenor}\
      El promedio de edades fue:{promedio}")