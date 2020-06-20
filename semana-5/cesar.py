class Ascii():

  def __init__(self):
    pass
  
  def ascii(self,caracter):
    return ord(caracter)

  def caracter(self, ascii):
    return chr(ascii)

objeto=Ascii()

print(objeto.ascii('@'))
print(objeto.caracter(75))