datos=[]
lista = []
dic ={}
nombre=input("ingrese el nombre: ")
for x in range(10):
    compra=float(input("ingrese el valor de la compra: "))
    if compra >= 500 and compra <= 1000:
        descuento=compra*0.50
        compras= compra-descuento
    if compra >=1 and compra <500:
        descuento=compra*0.20
        compras= compra-descuento
    datos.append(compras)

dic[nombre] = datos
promedio=sum(datos)/len(datos)
mayor=max(datos)
menor=min(datos)
print(f"el mayor es{mayor}\nel menor es de {menor}")

print(f"el promedio es de{promedio} \n el dicionario es{dic}")
