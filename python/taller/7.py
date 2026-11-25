listaEdades=[]
for x in range(1,11):
    edad=int(input("Digita tu edad:"))
    if edad<1 and edad>50:
        print("Paso el limite, edad no contada")
    else:
        listaEdades.append(edad)
total=sum(listaEdades)
mayor=max(listaEdades)
menor=min(listaEdades)
promedio=total/len(listaEdades)

print(f"Promedio de sueldos:{promedio}\n \
       sueldo mayor:{mayor}\n \
       sueldo menor:{menor}\n \
       total de sueldos:{total}")