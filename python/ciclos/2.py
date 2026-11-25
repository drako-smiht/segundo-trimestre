CantidadSueldos= int(input( "Ingrese la cantidad de sueldos:"))
ContadorSueldo=0
ContadorPersonasMenos=0
ContadorPersonasMas=0
ContadorM=0
ContadorF=0

for x in range (CantidadSueldos):
    Nombre= str(input("Digita el nombre:"))
    Sexo= str(input ("Digita el el sexo (f/m):"))
    Sueldo= float(input("Digita el sueldo de la persona:"))

    if Sexo == 'f':
        ContadorF += 1
    elif Sexo == 'm':
        ContadorM += 1

    if Sueldo > 1 and Sueldo < 300 and Nombre == 'Andres':
        if Sexo == 'm':
            AumentoSueldo = Sueldo * 0.2
            Total = AumentoSueldo + Sueldo
            ContadorSueldo += Total
        else:
            print('Un nombre de un hombre no puede ser femenino')
            ContadorSueldo += Sueldo
            
    elif Sueldo >= 300 and Sueldo < 600 and Nombre == 'Felipe':
        if Sexo == 'm':
            AumentoSueldo = Sueldo * 0.1
            Total = AumentoSueldo + Sueldo
            ContadorSueldo += Total
        else:
            print('Un nombre de un hombre no puede ser femenino')
            ContadorSueldo += Sueldo
            
    else:
        ContadorSueldo += Sueldo

    if Sueldo < 500:
        ContadorPersonasMenos += 1
    elif Sueldo >= 500: 
        ContadorPersonasMas += 1

if CantidadSueldos > 0:
    promedio = ContadorSueldo / CantidadSueldos
else:
    promedio = 0

print("El promedio de sueldos es:", promedio)
print("Personas que ganan menos de 500:", ContadorPersonasMenos)
print("Personas que ganan 500 o más:", ContadorPersonasMas)
print("Total de mujeres:", ContadorF)
print("Total de hombres:", ContadorM)