listaNotas=[]
listaPerdidas=[]
listaGanadas=[]
for x in range(1,11):
    sexo=str(input("Digita tu sexo (m o f):"))
    nota=int(input("Digita tu nota:"))
    if sexo=="f":
        totalNota=nota-3
        listaNotas.append(totalNota)
        listaPerdidas.append(totalNota)
    else:
        totalNota=nota+2
        listaNotas.append(totalNota)
        listaGanadas.append(totalNota)

promedioPerdidas=sum(listaPerdidas)/len(listaPerdidas)
promedioGanadas=sum(listaGanadas)/len(listaGanadas)
promedioGeneral=(sum(listaGanadas)+sum(listaPerdidas))/(len(listaPerdidas)+len(listaGanadas))

print(f"perdieron:{(len(listaPerdidas))}\n ganaron:{(len(listaGanadas))} \
        nota mayor:{(max(listaGanadas))}\n nota menor:{(min(listaPerdidas))}")
print(f"nota Promedio perdidas:{promedioPerdidas} \
        nota promedio ganadas:{promedioGanadas} \
         promedio de todas las notas:{promedioGeneral}")

