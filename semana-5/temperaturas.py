class temperaturas():
    def init(self):
        pass
    
    def celcius(self):
       repetir="S"
       while repetir=="S" or repetir=="s" :
           celcius=[]
           farenheit=[]
           lista=[]
           print ("=======++++++++++++++++=======") 
           archivo= input("Escribe el nombre del archivo:\n=======++++++++++++++++=======\n") #se pide de archivo#
           abrir= open(archivo, "r") 
           leer= abrir.read() 
           print(leer) 
           print("***************************************")
           abrir= open(archivo, "a")
           for convertir in leer:
               cantidad=int(input("¿Cantidad de temperaturas? "))
               cont=0
               promedio=0
               i=1
               while (cantidad>0):
                       cont+=1
                       celcius=float(input("ingresa tu temperatura en celcius\n"+"Número: " +str(i)+":")) 
                       lista.append(celcius)
                       i=i+1
                       cantidad=cantidad-1 
                       farenheit= celcius*1.8+32
                       piInString = str(celcius)
                       piInString2 = str(farenheit)
                       abrir.write(str("\n"+piInString))
                       abrir.write(str("\n"+piInString2)) 
                       print("los grados en celcius son:\n",celcius, "\nlos grados en farenheit son: \n", farenheit)
               repetir =input("¿desea repetir?\nS/N\n")
               if repetir == "N" or repetir == "n":
                   print ("===================================================") 
                   print("Gracias por usar codigo convertidor de temperaturas")
                   print ("===================================================")
                   abrir= open(archivo, "a")
                   for convertir in leer:
                       promedio=(promedio+celcius)/cont  
                       piInString3 = str(promedio)
                       abrir.write(str("\n"+piInString3))
                       print("Promedio "+str(promedio))
                       break
                       
                   break
                   abrir.close()
                       
objeto=temperaturas() 
objeto.celcius()