listaSueldos=[]
for x in range(1,11):
    sueldos=int(input("Digita tu sueldo:"))
    if sueldos<1 and sueldos>1000:
        print("Paso el limite, sueldo no contado")
    else:
        listaSueldos.append(sueldos)
total=sum(listaSueldos)
mayor=max(listaSueldos)
menor=min(listaSueldos)
promedio=total/len(listaSueldos)

print(f"Promedio de sueldos:{promedio}\n \
       sueldo mayor:{mayor}\n \
       sueldo menor:{menor}\n \
       total de sueldos:{total}")