class Ascii():
  texto=""
  if texto==texto.upper () :
    abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
  
  else:
    abc="abcdefghijklmnñopqrstuvwxyz"
  
  tipo=int(input("Ingrese el tipo de trabajo a realizar |\n1:Encriptar 2:Desencriptar|\ningrese numero\n"))
  texto =""

  def __init__(self):
    pass
  if tipo==1:
    def ascii(self,texto):
      cifrado=0
      texto=input("ingrese su cadena de texto\n")
      for c in texto:
        if c in abc:
          cifrad += abc(abc.index(c)+k%(len(abc)))
        else:
          cifrad+=c
          return ord(texto)

  def caracter(self, ascii):
    return chr(ascii)

objeto=Ascii()

print(objeto.ascii(caracter))
print(objeto.caracter(75))


