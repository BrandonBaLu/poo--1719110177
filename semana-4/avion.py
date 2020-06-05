
class avion:
   
  "atríbutos"
  alas= 2
  acientos = 416
  pilotos= 2
  volantes= 2
  ventanillas= 60
  
  #métodos

  def encender(self):
    print("encender")

  def apagar(self):
    print("volar")

  
  def __init__(self):
    pass

        

class Boeing(avion):
  
  #atríbutos
  
  Capacidad_de_pasajeros= 416.
  longitud= "70,66 m."

  #métodos

  def  velocidad_maxima(self):
    print("Velocidad máxima: 528 nudos")

  def transportarse(self):
    print("transportarse")

  def __init__(self):
    print("constructor de un avíon Boeing 747")
    def encender(self):
      print("encender avíon")
    pass

Boeing_747 = Boeing()

print("alas= "+str(Boeing_747.alas))
print("acientos= "+str(Boeing_747.acientos))
print("pilotos= "+str(Boeing_747.pilotos))
print("libretas= "+str(Boeing_747.volantes))
print("ventanillas= "+str(Boeing_747.ventanillas))
print("Capacidad de pasajeros= "+str(Boeing_747.Capacidad_de_pasajeros))
print("longitud= "+str(Boeing_747.longitud))
Boeing_747.encender()
Boeing_747.apagar()
Boeing_747.velocidad_maxima()
Boeing_747.transportarse()
