class coche:
   
  "atríbutos"
  puertas=4
  capasidad= 5
  asientos=6
  color= "AMARILLO"
  aire= "con aire acondicionado"
  
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
    pass

cheroke_2004 = Boeing()

print("alas= "+str(cheroke_2004.alas))
print("acientos= "+str(cheroke_2004.acientos))
print("pilotos= "+str(cheroke_2004.pilotos))
print("libretas= "+str(cheroke_2004.volantes))
print("ventanillas= "+str(cheroke_2004.ventanillas))
print("Capacidad de pasajeros= "+str(cheroke_2004.Capacidad_de_pasajeros))
print("longitud= "+str(cheroke_2004.longitud))
cheroke_2004.encender()
cheroke_2004.apagar()
cheroke_2004.velocidad_maxima()
cheroke_2004.transportarse()

class coche:
  placas= "hkk5846"
  modelo=2005
  
  rines= "rines modernos"
  frenos="frenos de disco"
  llantas=" 4 llantas"

  def arrancar(self):
    print("Arrancar")
  def acelerar(self):
    print(acelerar)
  def frenar(self):
    print("Frenar")
  def conbustible(self):
    print("gasolina")
  def apagar(self):
    print("apagar") 
  
  def _init_(self):
    print("GMC")
    print("placas="+str(self.placas))
    print("modelo="+str(self.modelo))
    print("puertas="+ str(self.puertas))
    print("capacidad="+ str(self.capasidad))
    print(self.asientos)
    print("color="+str(self.color))
    print(self.aire)
    print(self.rines)
    print(self.frenos)
    print("No. de llantas="+str(self.llantas))

objeto =coche()
objeto.arrancar()
objeto.frenar()
objeto.conbustible()
objeto._init_()