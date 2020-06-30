class cesar: #declare mi clase llamada cesar
  def archivo(self): #definí mi metodo llamado archivo para poderlo llamar al final como objeto
    repetir ="s" #difiní mi variable para mi ciclo while
    while repetir == "S" or repetir =="s": #puse mi condicion, si repetir esa igual a eso que se repita todo
      codificar= "" #declare mis variables 
      descifrar = "" 
      print ("========++++++++++++++++========") #imprimí mis decoraciones, me robe la idea de soloLern
      archivo= input("*Escribe el nombre del archivo:*\n========++++++++++++++++========\n") #se solicita el nombre del archivo para llamarlo
      abrir= open(archivo, "r") #abre el archivo para leerlo
      leer= abrir.read() #lee el archivo
      print(leer) #lo imprime
      print("**Brandon Balderas Lucas**")#puse mi nombre jaja
      tipo= int(input("====¦1:Codificar¦=======\n====¦2:descodificar¦====\n"+"*****UTEC TULANCINGO*****\n"))#definí mi variable tipo para que el usuario decidiera que quiere hacer en el programa
      if tipo==1: #si tipo es igual a 1 lo que hara sera codificar el texto
        abrir= open(archivo, "a")#abre el archivo ingresado 
        for traducir in leer: #en un rango de lalectura de lo que contenga el archivo lo encripta
          letras= ord(traducir) #encripta las letras 
          codificar+= chr(letras-2)
        abrir.write(codificar) #Reescribe el archivo
        print("\n",codificar ) #imprime la el archivo codificado
        abrir.close() #cierra el archivo
      if tipo==2:#si tipo es igaul a dos dessencrita el archivo que ingreses
        abrir= open(archivo, "a") #abre el archivo ingresado
        for traducir in leer: #en un rango de lo que mida el archivo lo descifra el texto
          letras= ord(traducir) 
          descifrar+= chr(letras+2)#desencripta el texto
        abrir.write(descifrar ) #abre el archivo y escribe el descifrado enseguida
        print("\n",descifrar ) #inprime lo que descifro
        abrir.close() 
      repetir =input("¿desea repetir?\nS/N\n") #pregunta al usuario si quiere volver a repetir el proceso
      if repetir == "N" or repetir == "n":#si la espuesta es n o N enseguida inprime la decoracion junto con el agradecimiento por usar codigo cesar y de inmediato rompe el ciclo
          print ("==============================") 
          print("*Gracias por usar codigo cesar*")
          print ("==============================") 
          break#rompe la iteracion 
objeto=cesar() #iguale mi clase con mi objeto
objeto.archivo()#mando a traer mi metodo
