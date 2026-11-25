def calcular_suscriptores(videos):
    total = 0

    while videos >= 1:
        supsnuevos = float(input("Ingrese la cantidad de subs que hizo el video:"))
        total = total + supsnuevos
        videos = videos - 1

        if total >= 100000:
            print("Ya tienes mas de 100 mil subs superaste la meta")
    
    print(total)


cantidadInicial = int(input("Cuantos videos subiste:")) 
c = calcular_suscriptores(cantidadInicial)