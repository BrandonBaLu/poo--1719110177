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
      if respuesta==1: 
        abrir= open(archivo, "a")
        for cambiar in leer: 
          letras= ord(cambiar) 
          codificar+= chr(letras-2)
        abrir.write(codificar) 
        print("\n",codificar ) 
        abrir.close() 
      if respuesta==2:
        abrir= open(archivo, "a")
        for cambiar in leer: 
          letras= ord(cambiar)  
          descifrar+= chr(letras+2)
        abrir.write(descifrar ) 
        print("\n",descifrar ) 
        abrir.close() 
      repetir =input("¿desea repetir?\nS/N\n") 
      if repetir == "N" or repetir == "n":
          print ("==============================") 
          print("*Gracias por usar codigo cesar*")
          print ("==============================") 
          break
objeto=cesar() 
objeto.tipo()