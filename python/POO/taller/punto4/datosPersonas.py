from claseRango import Person

for x in range(1,5):
    nombre=input("Ingrese el nombre:")
    precio=float(input("Ingrese el precio:"))

    objetoPersona=Person(nombre,precio)
    objetoPersona.comparacion()
objetoPersona.calculo()