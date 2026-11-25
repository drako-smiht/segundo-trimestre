diccionarioVentas={}
ventas=[]
t="si"
while t=="si":
    NombreEmpleado=str(input("Nombre:"))
    TotalVentas=int(input("Digita el dinero de hoy:"))
    diccionarioVentas["Vendedos:"+NombreEmpleado]="Monto"+str(TotalVentas)
    ventas.append(TotalVentas)
    t=str(input("Desea continuar (si|no):"))
suma=sum(ventas)
print(f"El total recaudado es de:{suma}\n\
      {diccionarioVentas}")
