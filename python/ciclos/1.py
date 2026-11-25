

perso =int (input ( "cuantas personas van a ingresar:"))

contador1= 0
contador2= 0
contador3= 0
contador4= 0
contador5= 0


for x in range (perso):
  Estrato= int (input ("Digite el estrato :"))
  edad = int (input ("Digite la edad:"))
  valor = float (input ("valor de la boleta:"))


  if Estrato == 1 and edad<18:
      des= valor*0.2
      contador1=valor-des
      contador1+=contador1
      
  elif Estrato == 1 and edad>=18 and valor<100:
     des= valor*0.15
     contador1=valor - des
     contador1+=contador1

  elif Estrato == 2 and edad>=18 and valor<=100:
     des= valor*0.1
     contador2=valor - des
     contador2+=contador2

   
  elif Estrato == 3 and edad>=18 and valor<=100:
        des= valor*0.05
        contador3=valor - des
        contador3+=contador3
  elif Estrato == 4 and edad>=18 and valor<=100:
        des= valor*0.05
        contador4=valor-des
        contador4+=contador4

  elif Estrato == 5 and edad>=18 and valor<=100:
       des= valor*0.05
       contador5=valor-des
       contador5+=contador5
    
  elif Estrato == 6:
      print (" solo hay 5 estratos")
      break



total= contador1+contador2+contador3+contador4+contador5

print(" El total recaudado fue de:" ,total)       
        
        
              
         