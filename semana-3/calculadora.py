class calculadora:

   
  "atríbutos"
  cajeros= 5
  personal= 30
  sillas= 15
  pantallas_llama_turnos= 4
  ventanillas= 12
  
  #métodos

  def retirar(self):
    print("retirar")

  def depositar(self):
    print("depositar")

  
  def __init__(self):
    pass

        

class azteca(banco):
  
  #atríbutos
  
  abierto_tarde="10 pm"
  entrega="entrega inmediata"

  #métodos

  def  prestamos(self):
    print("prestamos de forma inmediata")

  def abonos(self):
    print("abonos pequeños semanales")

  def __init__(self):
    print("constructor banco azteca")
    pass

elektra = azteca()

print("abierto hasta las= "+str(elektra.abierto_tarde))
print(elektra.entrega)
print("cajeros= "+str(elektra.cajeros))
print("personal= "+str(elektra.personal))
print("sillas= "+str(elektra.sillas))
print("pantallas llama turnos= "+str(elektra.pantallas_llama_turnos))
print("ventanillas= "+str(elektra.ventanillas))

elektra.retirar()
elektra.depositar()
elektra.prestamos()
elektra.abonos()

  
  
  
  
  funciones= 500
  multiplicacion="multiplicacion"
  teclas= 50
  tipo= "cientifica"
  modelo= "126Clc"
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
