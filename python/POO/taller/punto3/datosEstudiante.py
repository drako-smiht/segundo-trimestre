from claseEstudiante import Estudiante
nombre=input("Nombre del estudiante:")
preguntarNotas=int(input("Cuantas notas tiene el estudiante:"))

for x in range(preguntarNotas):
    notas=float(input("Digite la nota:"))
    objetoEstudiante=Estudiante(nombre,notas)

objetoEstudiante.calculos()

objetoEstudiante.decision()