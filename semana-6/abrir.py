class temperaturas():#Definí  mi clase
    def _init_(self):#Defií mi constructor 
        pass
    
    def celcius(self):#definí mi metodo
       repetir="S"#declare mi variable de repetir
       while repetir=="S" or repetir=="s" :#definí mi ciclo while
           #definí mis variables de temperaturas y la lista donde se guardo las temperaturas  
           celcius=[]
           farenheit=[]
           lista=[]
           fecha=[]#declare mi variable de fechas
           print ("=======++++++++++++++++=======") 
           archivo= input("Escribe el nombre del archivo:\n=======++++++++++++++++=======\n") #se pide de archivo
           abrir= open(archivo, "r")#abrí elarchivo
           leer= abrir.read() #lee el archivo
           print(leer) #leé el archivo
           print("***************************")
           abrir= open(archivo, "a")#abre el archivo y añade los datos ingresados
           for convertir in leer:#en un rango de tamaño del archivo realiza lo siguiente
               fecha.append(input("ingresar la fecha:\n"))#pide la fecha y ala guarda en fecha
               cantidad=int(input("¿Cantidad de temperaturas? "))#pide cuantas veces agregara temperaturas
               cont=0#declare mi contador
               i=1#inicie mi contador i a 1, esto para marcar que el numero de veces que pedira las temperaturas 
               while (cantidad>0):#declare mi cico para decir que mientras el numero de veces sea mayor a 0 
                       cont+=1#aumente mi contador mas 1
                       celcius=float(input("ingresa tu temperatura en celcius\n"+"Número: " +str(i)+":")) #pedí mis temperaturas en celcius
                       lista.append(celcius)#guarde mis temperaturas de celcuis en lista
                       i=i+1#aumente mi contador 
                       cantidad=cantidad-1 #reste la cantidad del numero de veces a pedir el archivo
                       farenheit= (celcius*1.8) +32#declare mi formula para la convercion
                       piInString = str(celcius)#converti mis valores de celcius a valores tipo strig
                       piInString2 = str(farenheit)#convertí mi mis valores de farenheit a str para guardarlos en el archivo
                       abrir.write(str("\nlos celcius son: "+piInString))#escribe en el archivo los celius
                       abrir.write(str("\nlos Farenheit son: "+piInString2)) #se escriben en el archivo los farenheit
                       print("los grados en celcius son:\n",celcius, "\nlos grados en farenheit son: \n", farenheit)
               repetir =input("¿desea repetir?\nS/N\n")#pregunde si queria repetir y si repetir es igial a s volvera a hacer todo de nuevo
               if repetir == "N" or repetir == "n":#si la respuesta es no 
                   print ("===================================================") 
                   print("*Gracias por usar codigo convertidor de temperaturas*")
                   print ("===================================================")#agradecí por usar la app
                   abrir= open(archivo, "a")#abrí rl archivo y añadí los datos al archivo
                   for convertir in leer:#en un rango de leer el archivo realizara lo siguiente 
                       cont+=1 #aumente mi contador 
                       promedio=celcius +farenheit /cont #declare mi vatiable promedio con su formula     
                       piInString3 = str(promedio)#converti el promedio a str
                       print ("el promedio de temperaturas es: " + piInString3) #imprimi mi promedio
                       abrir.write(str("\nEl promedio de temperaturas es: "+piInString3))#escribí los resultados del promedio en el archivo
                       celcius1=str(celcius)#iguale mi nueva variable con str
                       fecha_mayor=str(fecha)+max(celcius1)#mando a llamar la temperatura mas alta con la fecha mas alta
                       print ("la fecha con mayor temperatura es: " +str(fecha_mayor)) #imprimo la fecha mayor
                       break
                       
                   break
                   abrir.close()
           
            

objeto=temperaturas() #igualo mi objeto a temperaturas
objeto.celcius()#mando a traer mi metodo

  