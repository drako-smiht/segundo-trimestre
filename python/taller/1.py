sexo=str(input("Digita tu sexo (m o f):"))
edad=int(input("DIgita tu edad:"))

if edad>=18:
    if sexo=="m":
        print(f"Eres mayor de edad\n\
              y eres masculino")
    else:
        print(f"Eres mayor de edad\n\
              y eres mujer")
else:
    if sexo=="m":
         print(f"Eres menor de edad\n\
              y eres masculino")
    else:
         print(f"Eres menor de edad\n\
               y eres mujer")