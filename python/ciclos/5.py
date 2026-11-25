contra="santy"
intentos=0
while True:
    contraseña=input("Ingrese su contraseña:")
    if contraseña==contra:
        print("Ingreso correctamenre")
        break
    else:
        intentos+=1
        print(f"intento numero:{intentos}")

    if intentos>7:
        print("Limite de intentos alcanzado, reinicie")
        break
