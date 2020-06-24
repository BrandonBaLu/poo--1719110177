class cesar:

  def _init_(self):
    pass

  def ascii(self):
    texto =input("ingresa tu texto\n")
    for texto in texto:
      print("El valor de {} es {}".format(texto, ord(texto)))
  
  def descodificar (self):
    numeros=int(input("ingresa tus valores en numeros enteros\n"))
    for numero in numeros:
      print("El carácter que representa a {} es {}".format(numero, chr(numero)))

repetir="s"
while repetir=="s" or repetir=="S":
  objetoCesar = cesar()
  tipo=int(input("¿Que deseas hacer?\n¦1:cifrar¦\n¦2:descifrar¦\ningresa el numero de lo que deseas hacer\n"))
  if tipo==1:
    objetoCesar.ascii()
  if tipo==2:
    objetoCesar.descodificar()
  repetir=input ("¿Desea repetir? S/N\n")
  