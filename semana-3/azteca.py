class banco:
   
  "atributos"
  cajeros= 5
  personal= 30
  sillas= 15
  pantallas_llama_turnos= 4
  ventanillas= 12

  "atributos" 
  def __init__(self):
     print("Constructor de bancos")
     print("cajeros= "+str(self.cajeros))
     print("personal= "+str(self.personal))
     print("sillas= "+str(self.sillas))
     print("pantallas llama turnos= "+str(self.pantallas_llama_turnos))
     print("ventanillas= "+str(self.ventanillas))

  
  
  "métodos"
  def retirar(self):
    print("retirar")

  def depositar(self):
    print("depositar")
    
    

class azteca(banco):  
  
  def __init__(self):
    print("constructor de banco Azteca")
    print("cajeros= "+str(self.cajeros))
    print("personal= "+str(self.personal))
    print("sillas= "+str(self.sillas))
    print("pantallas llama turnos= "+str(self.pantallas_llama_turnos))
    print("ventanillas= "+str(self.ventanillas))



objeto = banco()
objeto.retirar()
objeto.depositar()

objeto_azteca = azteca()
objeto_azteca.retirar()
objeto_azteca.depositar()



  





















    
