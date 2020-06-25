class cesar:#primero declare mi clase

  def _init_(self):#definí mi constructor
    pass

  def ascii(self): #por otro lado definí mi metodo en donde se generara el cifrado
    texto =input("ingresa tu texto\n")#pedi que el usuario ingresara su cadena de texto
    for texto in texto:#en un rango de lo que mide la cadena pedi que codificara el texto
      print("El valor de {} es {}".format(texto, ord(texto)))
  
  def descodificar (self):
    numeros=int(input("ingresa tus valores en numeros enteros\n"))
    for numero in numeros:
      print("El carácter que representa a {} es {}".format(numero, chr(numero)))

repetir="s"
while repetir=="s" or repetir=="S":
  objetoCes2ar = cesar()
  tipo=int(input("¿Que deseas hacer?\n¦1:cifrar¦\n¦2:descifrar¦\ningresa el numero de lo que deseas hacer\n"))
  if tipo==1:
    objetoCesar.ascii()
  if tipo==2:
    objetoCesar.descodificar()
  repetir=input ("¿Desea repetir? S/N\n")
  