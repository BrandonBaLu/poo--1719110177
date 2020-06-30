class cesar:
  def _init_(self): 
    pass
  def tipo(self):
    repetir ="s" 
    while repetir == "S" or repetir =="s": #si le elige s o S se vuelve a correr el programa#
      codificar= "" 
      descifrar = "" 
      print ("=======++++++++++++++++=======") 
      archivo= input("Escribe el nombre del archivo:\n=======++++++++++++++++=======\n") #se pide de archivo#
      abrir= open(archivo, "r") 
      leer= abrir.read() 
      print(leer) 
      print("********")
      respuesta= int(input("====¦1:Codificar¦=======\n====¦2:descodificar¦====\n"+"********\n"))
      if respuesta==1: #cualquiera que se la obcion se ejecuta lo siguiente #
        abrir= open(archivo, "a") #se abre el arcivo y se adjunta por eso la letra a#
        for cambiar in leer: #se define el rango#
          letras= ord(cambiar) #se hace un cambio de caracteres#
          codificar+= chr(letras-2)#se resta 1 justo como funcina el codigo ASCII#
        abrir.write(codificar) #Se lee la variable a codificar#
        print("\n",codificar ) 
        abrir.close() 
      if respuesta==2:
        abrir= open(archivo, "a") #se abre el arcivo y se adjunta por eso la letra a#
        for cambiar in leer: #se define el rango#
          letras= ord(cambiar)  
          descifrar+= chr(letras+2)
        abrir.write(descifrar ) 
        print("\n",descifrar ) 
        abrir.close() 
      repetir =input("¿desea repetir?\nS/N\n" ) #pregunta si quieres repetir la operacion#
      if repetir == "N" or repetir == "n":
          print ("==============================") 
          print("*Gracias por usar codigo cesar*")
          print ("==============================") 
          break
objeto=cesar() 
objeto.tipo()