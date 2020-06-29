class cesar:
  texto=""

  def init(self, texto):
    self.texto=texto

  def codificar(self):

    cif=""
    for texto in self.texto:
        numeros= ord(texto)
        cif += chr(numeros + 2)
        print("El valor de {} ".format(cif))
    
  
  def descodificar (self):
      des=""
      for texto in self.texto:
        numeros= ord(texto)
        des += chr(numeros - 2)
       print("El valor de {} ".format(des))


repetir="s"
while repetir=="s" or repetir=="S":
  
  tipo=int(input("que deseas hacer\n|1:cifrar\n2:descifrar\n"))
  texto =input("ingresa tu texto\n")
  objetoCesar = cesar()
  if tipo==1:
    objetoCesar.codificar()
  if tipo==2:
    objetoCesar.descodificar()
  repetir=input ("¿Desea repetir? S/N\n")