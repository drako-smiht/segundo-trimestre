from claseSexos import Person
for x in range(1,5):
    sexo=input("Digite su sexo(f|m):")
    nota=float(input("Digite su nota:"))
    objetoPersona=Person(sexo,nota)
    objetoPersona.comparacion()
objetoPersona.calculos()