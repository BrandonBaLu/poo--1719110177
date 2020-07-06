class temperaturas():#definí mi clase
    def init(self):#definí mi constructor
        pass
    
    def celcius(self):#defií mi metodo
       repetir="S"#le di a mi variable repetir su valor
       while repetir=="S" or repetir=="s" :#mientras se cumpla las condiciones de este ciclo while, este se repetira
           celcius=[]#declare mis variables de tipo lista
           farenheit=[]
           lista=[]
           print ("=======++++++++++++++++=======") 
           archivo= input("Escribe el nombre del archivo:\n=======++++++++++++++++=======\n") #se solicita el archivo a utolizar
           abrir= open(archivo, "r") #abre el arhivo 
           leer= abrir.read()#leé el archivo 
           print(leer) #imprime el archivo
           print("***************************************")
           abrir= open(archivo, "a")#se añaden los datos de las temperaturas al archivo
           for convertir in leer:#en un rango del archivo convierte las temperaturas celcius a farenheit
               cantidad=int(input("¿Cantidad de temperaturas? "))#solicita una cantidad de temperaturas que el usuario desée ingresar
               cont=0#inicializo mis contadores en cero para despues utilizarlo
               promedio=0
               i=1
               while (cantidad>0):#mientas la cantidad de temperaturas que el usuario desea ingresar sea mayor a cero hara la convercion 
                       cont+=1#aumento mi contador para utilizarlo en el promedio
                       celcius=float(input("ingresa tu temperatura en celcius\n"+"Número: " +str(i)+":")) #pido los valores en celcius
                       lista.append(celcius)#recabo las temperaturas reabadas
                       i=i+1#aumento mi contador
                       cantidad=cantidad-1 #aumento mi contador para que aumente el numero de la cantidad 
                       farenheit= celcius*1.8+32#ingreso mi formula para convertir mis grados celcius a farenheit
                       piInString = str(celcius)#igualo mis variables tipo float a un string 
                       piInString2 = str(farenheit)#igualo mis variables tipo float a un string 
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
                       piInString3 = str(promedio)#igualo mis variables tipo float a un string 
                       abrir.write(str("\n"+piInString3))
                       print("Promedio "+str(promedio))
                       break
                       
                   break
                   abrir.close()
                       
objeto=temperaturas() 
objeto.celcius()