nombres=[]
precios=[]
for x in range(1,4):
    nombrePersonas=str(input("Ingrese el nombre:"))
    precio=int(input("Ingrese el precio "))
    if precio<1 or precio>1000:
        print("NO se puede ingresar un precio superior de 1000 o inferior a 1 ")
        break
    if nombrePersonas=="susana":
        aumento=precio*0.2
        total=aumento+precio
        nombres.append(nombrePersonas)
        precios.append(total)
    elif nombrePersonas=="jessica":
        aumento=precio*0.15
        total=aumento+precio
        nombres.append(nombrePersonas)
        precios.append(total)
    elif nombrePersonas=="wilson":
        aumento=precio*0.1
        total=aumento+precio
        nombres.append(nombrePersonas)
        precios.append(total)
    else:
        precios.append(precio)
        nombres.append(nombrePersonas)

promedio=sum(precios)/len(precios)
precioMayor=max(precios)
precioMenor=min(precios)
print(f"el promedio es:{promedio}\n\
      precio mayor:{precioMayor}\n\
        precio menor:{precioMenor}")