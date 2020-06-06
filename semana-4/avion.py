class avion:
   
  "atríbutos"
  alas= 2
  acientos = 416
  pilotos= 2
  volantes= 2
  ventanillas= 608
  
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
    print("encender avíon Boeing 747")
  def apagar(self):
    print("volar avion Boeing 747")
  def  velocidad_maxima(self):
    print("Velocidad máxima de un avíon Boeing 747 : 528 nudos")
  def transportarse(self):
    print("transportarse de un avíon Boeing 747")

Boeing_747 = Boeing()

print("alas del Boeing 747 = "+str(Boeing_747.alas))
print("acientos del Boeing 74= "+str(Boeing_747.acientos))
print("pilotos del Boeing 747 = "+str(Boeing_747.pilotos))
print("libretas del Boeing 747 = "+str(Boeing_747.volantes))
print("ventanillas del Boeing 747 = "+str(Boeing_747.ventanillas))
print("Capacidad de pasajeros del Boeing 747= "+str(Boeing_747.Capacidad_de_pasajeros))
print("longitud del Boeing 747 = "+str(Boeing_747.longitud))
Boeing_747.encender()
Boeing_747.apagar()
Boeing_747.velocidad_maxima()
Boeing_747.transportarse()
