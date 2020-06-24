class Ascii():
  texto=""
        
  tipo=int(input("Ingrese declare mi claseel tipo de trabajo a realdefini mi constructorizar \n|1:Encriptar 2:Desencriptar|\ning#defini mi metodo a llamarrese numero\n"))
    
 or reperir="s"  if tipo==1:
    def ascii(self,texto):
      texto = input("Mensaje cifrado > ").upper()
      nin = int(input("Desplazamiento > "))
      cifrado = ""
      if texto==texto.upper():
        abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
      else:
        abc="abcdefghijklmnñopqrstuvwxyz" #PARA MINUSCULAS
        for l in texto:
          if l in abc:
            pos_letra = abc.index(l)
            nueva_pos = (pos_letra + nin) % len(abc)
            cifrado+= abc[nueva_pos]
          else:
            cifrado+= l
            print("Mensaje cifrado:", cifrado)
objetoascii=Ascii(texto)
objetoascii.ascii

  
  





