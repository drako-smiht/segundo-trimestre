def imc_Persona (peso, altura):
    imc= peso/(altura**2)
    if imc>=30.0:
        return "Obeso"
    elif imc>=25.0 and imc<=29.9:
        return "Sobrepeso"
    elif imc>=18.5 and imc<=24.9:
        return "normal"
    else:
        return "bajo "

pesoPersona=float(input("Digita tu peso:"))
alturaPersona = float(input("Digita tu altura:"))

pa=imc_Persona(pesoPersona, alturaPersona)

print("Tu peso actual es:",pa)