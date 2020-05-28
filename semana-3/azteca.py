class banco:
   
  "atributos"
  cajeros= 5
  personal= 30
  sillas= 15
  pantallas_llama_turnos= 4
  ventanillas= 12
   
  def __init__(self):
     print("Constructor de bancos")

  def retirar(self):
    print("retirar")

  def depositar(self):
    print("depositar")
    
    
class azteca(banco):  
  
  def __init__(self):
    print("constructor de banco Azteca" )

objeto=banco()
objeto.retirar()
objeto.depositar()
objeto=azteca()
objeto.retirar()
objeto.depositar()
objeto.__init__()

  





















    
