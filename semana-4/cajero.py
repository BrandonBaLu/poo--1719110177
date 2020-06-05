class cajero:

   
  #atríbutos"

  funciones= 22
  gabeta= 1
  gabeta_billetes= 1
  impresora= 1
  teclas= 20
  
  #métodos

  def imprimir(self):
    print("imprime")
  
  def pagar(self):
    print("cierra gabeta")
  
  
  def __init__(self):
    pass

        

class cajeros(cajero):
  
  #atríbutos
  
  pantalla= "pantalla touch"
  color="gris"

  #métodos
  
  def cambio(self):
    print("cambiar dinero")
  
  def servicios(self):
    print("abre gabeta")

  def __init__(self):
    print("constructor de cajero elektra")
  
  def imprimir(self):
    print("imprime del cajero de elektra")
  
  def pagar(self):
    print("cierra gabeta del cajero de elektra")
  
  def cambio(self):
    print("cambiar dinero en el cajero de elektra")
  
  def servicios(self):
    print("abre gabeta del cajero de elektra")

  def __init__(self):
    print("constructor de cajero elektra")
    pass

cajero_BBVA = cajeros()

print("funciones del cajero de elektra ="+str(cajero_BBVA .funciones))
print("gabeta del cajero de elektra ="+str(cajero_BBVA .gabeta))
print("gabeta para billetes del cajero de elektra = "+str(cajero_BBVA .gabeta_billetes))
print("impresora del cajero de elektra = "+str(cajero_BBVA .impresora))
print("teclas del cajero de elektra "+str(cajero_BBVA .teclas))
print(cajero_BBVA.pantalla)
print("color del cajero de elektra= "+str(cajero_BBVA .color))


cajero_BBVA .imprimir()
cajero_BBVA .cambio()
cajero_BBVA .servicios()
cajero_BBVA .pagar()