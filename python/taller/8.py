listaPrecios=[]
precios=0
aumento=0
for x in range(1,11):
    nombre=str(input("Ingrese su nombre:"))
    precios=int(input("ingrese el precio "))
    if precios<1 and precios>1000:
        print("Precio no admitido")
    elif nombre=="susana":
        aumento=precios*1.20
        listaPrecios.append(aumento)
    elif nombre=="jessica":
        aumento=precios*1.15
        listaPrecios.append(aumento)
    elif nombre=="wilson":
        aumento=precios*1.10
        listaPrecios.append(aumento)
    else:
        listaPrecios.append(precios)

promedio=sum(listaPrecios)/len(listaPrecios)
total=sum(listaPrecios)
mayor=max(listaPrecios)
menor=min(listaPrecios)

print(listaPrecios)
print(f"promedio:{promedio}\n mayor:{mayor}\n menor:{menor}\n total:{total}")
        