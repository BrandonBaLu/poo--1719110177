class cesar:#primero declare mi clase
  t=0
  numeros=0  
  def _init_(self):#definí mi constructor
    pass

  def ascii(self): #por otro lado definí mi metodo en donde se generara el cifrado
  
    texto =input("ingresa tu texto\n")
    for t in texto:
      print("El valor de {} es {}".format(texto, ord(t))) 
      numeros=t
  
  def descodificar (self):
    dec = [] 
    texto =input("ingresa tu texto\n") 
    for i in range(len(texto)): 
     key_c = key[i % len(key)] 
     dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
     dec.append(dec_c)  
     print(chr(dec))
    

repetir="s"
while repetir=="s" or repetir=="S":
  objetoCesar = cesar()
  tipo=int(input("¿Que deseas hacer?\n¦1:cifrar¦\n¦2:descifrar¦\ningresa el numero de lo que deseas hacer\n"))
  if tipo==1:
    objetoCesar.ascii()
  if tipo==2:
    objetoCesar.descodificar()
  repetir=input ("¿Desea repetir? S/N\n")