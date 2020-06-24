class cesar:
   
  
  def __init__(texto):
    pass

  def ascii(self):
    texto =input("ingresa tu texto\n")
    for texto in texto:
        print("El valor de {} es {}".format(texto, ord(texto)))
  
  def descodificar (self):
    numeros=int(input("ingresa tus valores en numeros enteros\n"))
    for numero in numeros:
      print("El carácter que representa a {} es {}".format(numero, chr(numero))
      
repetir="s"
while repetir=="s" or repetir=="S":
  objetoCesar = cesar()
  objetoCesar.ascii()
  objetoCesar.descodificar
  repetir=input ("¿Desea repetir? S/N\n")
