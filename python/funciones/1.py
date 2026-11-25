def calcular_sueldo(horas , pago_hora):
    if horas > 40:
        extras = horas - 40
        total = (40 * pago_hora) + (extras * (pago_hora * 1.5))
    else:
        total = horas * pago_hora
    return total

otro = "si"

while otro == "si":
    h = float(input("escribe las horas q trabajo: "))
    p = float(input("escribe cuanto pagan por hora: "))

    resultado = calcular_sueldo(h , p)
    print("el sueldo de este man es " + str(resultado))

    otro = input("vas a calcular otro? (si/no): ")