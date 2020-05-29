class calculadora:

   
  "atríbutos"
  funciones= "funciones"
  multiplicacion="multiplicacion"
  teclas= 50
  tipo= "cientifica"
  forma="rectangular"
  
  #métodos

  def prender(self):
    print("Encender")

  def apagar(self):
    print("apagar")

  
  def __init__(self):
    pass

        

class casio(calculadora):
  
  #atríbutos
  
  funciones_c= 500
  color="roja"

  #métodos
  
  def  graficar(self):
    print("graficar")
    
  def dividir(self):
    print("dividir")

  def __init__(self):
    print("constructor de calculadora casio_126Clc")
    pass

casio_126Clc = casio()

print(casio_126Clc.funciones)
print(casio_126Clc.multiplicacion)
print("teclas= "+str(casio_126Clc.teclas))
print("tipo= "+str(casio_126Clc.tipo))
print("forma "+str(casio_126Clc.forma))
print("funciones casio 126Clc= "+str(casio_126Clc.funciones_c))
print("color= "+str(casio_126Clc.color))



casio_126Clc=casio()
casio_126Clc.prender()
casio_126Clc.apagar()
casio_126Clc.graficar()
casio_126Clc.dividir()


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
