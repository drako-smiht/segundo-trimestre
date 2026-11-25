diccionario={}
listaSueldos=[]
listaNombres=[]
for x in range(1,11):
    nombre=str(input("Digita el nombre:"))
    sueldo=int(input("Digita tu sueldo:"))
    if sueldo<1 and sueldo>1000:
        print("Sueldo no valido , no se le sumo.")
    elif sueldo<300 and nombre=="wilson":
        totalSueldo=sueldo*1.20
        listaSueldos.append(sueldo)
        listaNombres.append(nombre)
        diccionario[nombre]=sueldo
    elif sueldo>=300 and sueldo<600 and nombre=="Fredy":
        totalSueldo=sueldo*1.10
        listaSueldos.append(sueldo)
        listaNombres.append(nombre)
        diccionario[nombre]=sueldo
    else:
        listaSueldos.append(sueldo)
        listaNombres.append(nombre)
        diccionario[nombre]=sueldo

promedioSueldos=sum(listaSueldos)/len(listaSueldos)

print(f"Lista de nombres:{listaNombres}\
        Lista sueldos:{listaSueldos}\
        promedio sueldos:{promedioSueldos}\
        Diccionario:{diccionario}")

