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
  
  abierto_tarde="10 pm"
  entrega="entrega inmediata"

#métodos
def  prestamos_inmediatos(self):
  print("prestamos de forma inmediata")
def abonos_pequenos(self):
  print("abonos pequeños semanales")

def __init__(self):
  pass

elektra = azteca()


print("cajeros= "+str(elektra.cajeros))
print("personal= "+str(elektra.personal))
print("sillas= "+str(elektra.sillas))
print("pantallas llama turnos= "+str(elektra.pantallas_llama_turnos))
print("ventanillas= "+str(elektra.ventanillas))

elektra.retitar()
elektra.depositar()
elektra.prestamos_inmediatos()
elektra.abonos_pequenos()


  





















    
