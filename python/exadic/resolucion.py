diccionario={}
for x in range(1,3):
    nombre=str(input("Digita tu nombre:"))
    salario=float(input("Digita tu salario: "))
    diccionario [nombre]=salario
    listasuma=[]
for x, y in diccionario.items():
    listasuma.append(y)
    promedio=sum(listasuma)/len(listasuma)
print (f"el promedio es de:{promedio}\n\el diccionario: {diccionario}")