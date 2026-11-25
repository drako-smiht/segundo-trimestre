from notasSueldoEd import Persona

for x in range(1,5):
    sueldos=float(input("Digita tu sueldo:"))
    edades=int(input("Digita tu edad:"))
    notas=float(input("Digita tu nota:"))
    objetoPersona=Persona(sueldos,edades,notas)

objetoPersona.impresion()