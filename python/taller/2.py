numeros=[]
numero=0
for x in range(1,9):
    numero+=1
    numeros.append(numero)
mayor=max(numeros)
menor=min(numeros)
print(f"Mayor:{mayor}\n menor:{menor}")