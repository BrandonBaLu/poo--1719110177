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

  def depositar(self):
    print("depositar")

  
  def __init__(self):
    pass

        

class casio(calculadora):
  
  #atríbutos
  
  tamaño= "grande"
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

print("abierto hasta las= "+str(casio_126Clc.abierto_tarde))
print(casio_126Clc.entrega)
print("cajeros= "+str(casio_126Clc.cajeros))
print("personal= "+str(casio_126Clc.personal))
print("sillas= "+str(casio_126Clc.sillas))
print("pantallas llama turnos= "+str(casio_126Clc.pantallas_llama_turnos))
print("ventanillas= "+str(casio_126Clc.ventanillas))

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
    
