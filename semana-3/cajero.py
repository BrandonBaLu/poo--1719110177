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
  
  def  graficar(self):
    print("graficar")
    
  def dividir(self):
    print("dividir")

  def __init__(self):
    print("constructor de calculadora casio_126Clc")
    pass

casio_126Clc = casio()

print(casio_126Clc.funciones)
print(casio_126Clc.multiplicacion)
print("teclas= "+str(casio_126Clc.teclas))
print("tipo= "+str(casio_126Clc.tipo))
print("forma "+str(casio_126Clc.forma))
print("funciones casio 126Clc= "+str(casio_126Clc.funciones_c))
print("color= "+str(casio_126Clc.color))



casio_126Clc=casio()
casio_126Clc.prender()
casio_126Clc.apagar()
casio_126Clc.graficar()
casio_126Clc.dividir()


  class cajero:
  funciones= 22
  gabeta= "si"
  gabeta_billetes= 1
  retirar= "cantidad a retirar"
  depositar="juvenil"
  nombre= "Brandon BaLu"
  
  def imprimir(self):
    print("imprime")
  def cambio(self):
    print("cambiar dinero")
  def servicios(self):
    print("abre gabeta")
  def pagar(self):
    print("cierra gabeta")
  def resivir(self):
    print("contar dinero")
 
  def _init_(self):
    print("Futbolista")
    print(self.funciones)
    print(self.gabeta)
    print(self.gabeta_billetes)
    print(self.retirar)
    print(self.depositar)
    print(self.nombre)

objeto = cajero()
objeto.imprimir()
objeto.cambio()
objeto.servicios()
objeto.pagar()
objeto.resivir()
