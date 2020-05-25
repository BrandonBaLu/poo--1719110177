class Azteca:
  '''Atríbutos'''

  cajeros= "10"
  ventanillas= "10"
  personal= "30"
  sillas= "24"
  maquinas_de_turnos= "1"
  pantallas= "3"
  bocinas= "3"
  oficinas= "10"
  computadoras= "20"
  impresoras="2"
 
  '''Métodos'''
  def cuentas(self):
    print("crear cuentas bancarias")
  def ahorrar(self):
    print("ahorrar")
  def depositar(self):
    print("depositar")
  def retirar(self):
    print("retirar")
  def pagar(self):
    print("pagar servicios")  

  def _init_(self):
    print("atributos banco Azteca")
    print("cajeros="+str(self.cajeros))
    print("ventanillas"+str(self.ventanillas))
    print("personal="+str (self.personal))
    print("sillas="+str(self.sillas))
    print("maquina de turnos0"+str(self.maquinas_de_turnos))
    print("pantallas="+str(self.pantallas))
    print("bocinas="+str(self.bocinas))
    print("oficinas="+str(self.oficinas))
    print("computadoras="+str(self.computadoras))
    print("impresoras"+str(self.impresoras))
objeto = Azteca()
objeto.cuentas()
objeto.ahorrar()
objeto.depositar()
objeto.retirar()
objeto.pagar()
objeto._init_()
