t = "si"
diccionarioNotas = {}

while t == "si":
    nombre = str(input("Digita tu nombre: "))
    cantidad = int(input("Ingrese la cantidad de notas del estudiante: "))
    notas = []
    
    for n in range(cantidad):
        nota = float(input("Ingrese la nota del estudiante: "))
        notas.append(nota)
    
    diccionarioNotas[nombre] = notas 
    t = input("Desea continuar (si|no): ")

listaGanaron = []
listaPerdieron = []

for x, y in diccionarioNotas.items():
    promedio = sum(y) / len(y)
    
    if promedio >= 3.0:
        listaGanaron.append(x)
    else:
        listaPerdieron.append(x)


print(f"ganaron {len(listaGanaron)}: {listaGanaron}\n\
       perdieron {len(listaPerdieron)}: {listaPerdieron}")

