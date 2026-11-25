from explicacionProfe.clasebanco import cuenta

t="si"
while t=="si":
    saldoInicial =float(input("Ingrese el saldo inicial de la cuenta:"))
    cuen= cuenta(saldoInicial)

    while True:
        print("Opciones:\n\
              1.Depositar\n\
              2.Retirar\n\
              3.salir")
        opcion = input("Seleccione una opcion:")

        if opcion=="1":
            cantidad=float(input("Ingrese la cantidad a depositar:"))
            cuen.depositar(cantidad)
            print(f"Deposito realizado.Nuevo saldo:{cuen.saldo}")

        elif opcion=="2":
            cantidad=float(input("ingrese la cantidad a retirar:"))
            cuen.retirar(cantidad)
            print(f"Nuevo saldo:{cuen.saldo}")
        elif opcion=="3":
            break
        else:
            print("Opcion no valida.")
    t=input("Desea crear otra cuenta?(si|no):")