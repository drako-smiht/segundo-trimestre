from logicaDatos import MotoEsp


nombre = input("Ingrese el nombre de la moto: ")
marca = input("Ingrese la marca de la moto: ")
cilindraje = float(input("Ingrese el cilindraje de la moto: "))
tipoRepuesto = int(input("Ingrese el tipo de repuesto\n"
                         "1. Motor\n"
                         "2. Chasis\n"
                         "3. Cambio de aceite\n: "))

objetoMotoEsp = MotoEsp(nombre, marca, cilindraje, tipoRepuesto)

objetoMotoEsp.impresion()