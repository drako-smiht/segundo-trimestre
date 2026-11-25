listaNotas=[]
for x in range(1,7):
    nota=int(input("nota:"))
    listaNotas.append(nota)
promedio=sum(listaNotas)/len(listaNotas)
if promedio>=6:
    print(f"Gano con:{promedio}")
else:
    print(f"Perdio con:{promedio}")