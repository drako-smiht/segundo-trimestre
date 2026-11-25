notas=[]
ganaron=0
perdieron=0
sumaG=0
sumaP=0

for x in range(1,4):
    sexo=int(input("Cual es tu sexo(1:M\2:F):"))
    notasEstudiantes=float(input("Cual es tu nota:"))
    
    if sexo==2:
        nots=notasEstudiantes-3
    else:
        nots=notasEstudiantes+2
        
    notas.append(nots)
    
    if nots>=3:
        ganaron=ganaron+1
        sumaG=sumaG+nots
    else:
        perdieron=perdieron+1
        sumaP=sumaP+nots

if ganaron>0:
    promG=sumaG/ganaron
else:
    promG=0

if perdieron>0:
    promP=sumaP/perdieron
else:
    promP=0

print(f"Ganaron:{ganaron} prom:{promG}\n\
      Perdieron:{perdieron} prom:{promP}\n\
      Mayor:{max(notas)}\n\
      Menor:{min(notas)}")