class banco:
   
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
