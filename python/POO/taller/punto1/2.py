from impuesto import empleado

nombre=input("Ingrese su nombre:")
sueldo=float(input("Ingrese su sueldo:"))

persona = empleado(nombre,sueldo)

persona.impuesto(sueldo)
print(persona.nombre,persona.sueldo)