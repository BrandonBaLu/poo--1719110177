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
def abonos_pequeños(self):
  print("abonos pequeños semanales")


elektra = azteca()


print(elektra.cajeros)
print(elektra.personal)
print(elektra.sillas)
print(elektra.pantallas_llama_turnos)
print(elektra.ventanillas)



  





















    
