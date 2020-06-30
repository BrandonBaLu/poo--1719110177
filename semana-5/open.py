class archivo_vscesar: #clase principal#
  def _init_(self): #metodo constructor#
    pass
  def cifardesif(self):
    devolver="s" #Defina variable devolver#
    while devolver== "S" or devolver=="s": #si le elige s o S se vuelve a correr el programa#
      cif= "" #se alamacena el texto cifrar#
      desif= "" #se alamcena e texto a desifrar #
      textoarch= input("Nombre del archivo: ") #se pide de archivo#
      abrir= open(textoarch, "r") #abrimos el archivo y se usa la letra r porque es la inical de la palabra read y da alucion a leer#
      leer= abrir.read() #se lee el archivo#
      print(leer) #se imprieme lo que contiene l avariable leer#
 
      preguntar= input("¿Cifrar o desifrar?" ) #Se pregunta si desifra o cifra#
      if preguntar== "Cifrar" or preguntar== "cifrar": #cualquiera que se la obcion se ejecuta lo siguiente #
 
        abrir= open(textoarch, "a") #se abre el arcivo y se adjunta por eso la letra a#
 
        for cambiar in leer: #se define el rango#
          abesedario= ord(cambiar) #se hace un cambio de caracteres#
          cif+= chr(abesedario-1)#se resta 1 justo como funcina el codigo ASCII#
        abrir.write(cif) #Se lee la variable a codificar#
        print(cif) #imprime el texto guardo pero ya cifrado#
        abrir.close() #cierra el archivo#
      if preguntar== "desifrar" or preguntar== "Desifrar": #cualquiera que se opcion corre las siguientes lineas#
        abrir.open(textoarch, "a") #a de adjuntar asi que adjunta el archivo#
        for cambiar in leer: #los cambia al leguaje normal#
          abesedario= ord(cambiar) #se cmabia allenguaje matural#
          desif += chr(abesedario+1) #le suma uno para desifrarlo#
        abrir.write(desif) #lo escibre en el archivo de texto#
        abrir.close() #cierra el archivo#
        print(desif) #imprime el desifrado#
      devolver=input("¿Quiere repetir?" ) #pregunta si quieres repetir la operacion#
      if devolver== "N" or devolver== "n": #cualquiera que sea la opcion termina el proceso#
        break
objeto=archivo_vscesar() #se menciona la clase principal#
objeto.cifardesif() #se llama al objeto#