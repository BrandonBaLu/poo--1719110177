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
  
  def  sumar(self):
    print("sumar")

  def restar(self):
    print("restar")

  def __init__(self):
    print("constructor de un avíon Boeing 747")
    pass

casio_126Clc = casio()

print(casio_126Clc.funciones)
print(casio_126Clc.multiplicacion)
print("teclas= "+str(casio_126Clc.teclas))
print("tipo= "+str(casio_126Clc.tipo))
print("forma "+str(casio_126Clc.forma))
print("funciones casio 126Clc= "+str(casio_126Clc.funciones_c))
print("color= "+str(casio_126Clc.color))

casio_126Clc=calculadora()
casio_126Clc.prender()
casio_126Clc.apagar()
casio_126Clc.restar()
casio_126lc.sumar()

