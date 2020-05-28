  class futbolista:
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

objeto = futbolista()
objeto.imprimir()
objeto.cambio()
objeto.servicios()
objeto.pagar()
objeto.resivir()
objeto._init_()

