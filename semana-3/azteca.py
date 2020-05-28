class banco:
   
  "atríbutos"
  cajeros= 5
  personal= 30
  sillas= 15
  pantallas_llama_turnos= 4
  ventanillas= 12
  
  
  "métodos"
  def retirar(self):
    print("retirar")

  def depositar(self):
    print("depositar")

  
  def __init__(self):
    pass

    
    
    

class azteca(banco):
  """atríbutos"""
  def abierto_tarde="10 pm"
  entrega="entrega inmediata"


elektra=azteca()



objeto = banco()
objeto.retirar()
objeto.depositar()

objeto_azteca = azteca()
objeto_azteca.retirar()
objeto_azteca.depositar()



  





















    
