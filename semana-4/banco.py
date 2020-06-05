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
    print("constructor banco azteca en elektra")
  
  def retirar(self):
    print("retirar en elektra")

  def depositar(self):
    print("depositar en elektra")
  
  def  prestamos(self):
    print("prestamos de forma inmediata en elektra")

  def abonos(self):
    print("abonos pequeños semanales en elektra")
    pass

elektra = azteca()

print("abierto en elektra hasta las = "+str(elektra.abierto_tarde))
print(elektra.entrega)
print("cajeros en elektra = "+str(elektra.cajeros))
print("personal en elektra = "+str(elektra.personal))
print("sillas en elektra= "+str(elektra.sillas))
print("pantallas llama turnos en elektra = "+str(elektra.pantallas_llama_turnos))
print("ventanillas en elektra = "+str(elektra.ventanillas))

elektra.retirar()
elektra.depositar()
elektra.prestamos()
elektra.abonos()
