cantidadEstudiantes=int(input("Digite la cantidad de estudiantes:"))
contador=0
for x in range(cantidadEstudiantes):
    edad=int(input("Digite la edad del estudiante:"))
    contador+=1
if edad>=110:
    print("Edad muy alta")
    
elif edad<0:
    print ("Edad es baja")
    
promEstudiantes = (edad + edad)/contador
print(" El promedio de edades es:", promEstudiantes)
