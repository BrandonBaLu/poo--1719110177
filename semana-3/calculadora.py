class calculadora:

   
  "atríbutos"
  funciones= "funciones"
  multiplicacion="multiplicacion"
  teclas= 50
  tipo= "cientifica"
  forma="rectangular"
  
  #métodos

  def prender(self):
    print("Encender")

  def apagar(self):
    print("apagar")

  
  def __init__(self):
    pass

        

class casio(calculadora):
  
  #atríbutos
  
  funciones_c= 500
  color="roja"

  #métodos

  def sumar(self):
    print("sumar")
  
  def restar(self):
    print("restar")

  def __init__(self):
    print("constructor calculadora casio 126Clc")
    pass

casio_126Clc = casio()

print(casio_126Clc.funciones)
print(casio_126Clc.multiplicacion)
print("teclas= "+str(casio_126Clc.teclas)
print("tipo= "+str(casio_126Clc.tipo))
print("forma "+str(casio_126Clc.forma))
print("funciones casio 126Clc= "+str(casio_126Clc.funciones_c))
print("color= "+str(casio_126Clc.color))

casio_126Clc=calculadora()
casio_126Clc.prender
casio_126Clc.multiplica
casio_126Clc.sumar
casio_126Clc.restar

  
  
  
  
  
  modelo= "126Clc"
  marca= "CASIO"
  
  '''metodos'''
  
  def multiplica(self):
    print("multiplica") 
  
  
  
  def _init_(self):
    print("Calculadora Cientifica")
    print("funciones: "+ str(self.funciones))
    print("Realiza: "+str(self.multiplicacion))
    print(self.teclas)
    print(self.tipo)
    print(self.modelo)
    print(self.marca)
    print(self.tama)
    print(self.forma)
    print(self.color)
    
