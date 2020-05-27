class calculadora:
  funciones= 500
  multiplicacion="multiplicacion"
  teclas= 50
  tipo= "cientifica"
  modelo= "STR25"
  marca= "CASIO"
  tama= "grande"
  forma="rectangular"
  color="roja"
  '''metodos'''
  def prender(self):
    print("Encender")
  def multiplica(self):
    print("multiplica") 
  def sumar(self):
    print("sumar")
  def restar(self):
    print("restar")
  def apagar(self):
    print("Apagado automatico")
  
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
    
objeto=calculadora()
objeto.prender
objeto.multiplica
objeto.sumar
objeto.restar
objeto._init_()
