class coche:
   
  "atríbutos"
  puertas= 4
  capacidad= 10
  asientos= 6
  color= "AMARILLO"
  aire= "con aire acondicionado"
  
  #métodos

  def encender(self):
    print("encender")

  def apagar(self):
    print("volar")

  
  def __init__(self):
    pass

        

class Grand_cheroke(coche):
  
  #atríbutos
  
  volante= "volantes con cruice and set"
  frenos="frenos de aire"

  #métodos

  def  velocidad_maxima(self):
    print("Velocidad máxima: 200 km/h")

  def arrancar_control(self):
    print("arrancar a control remoto")

  def __init__(self):
    print("constructor de Grand Cherokee 2004")
    pass

cheroke_2004 = Grand_cheroke()

print("puertas= "+str(cheroke_2004.puertas))
print("capacidad= "+str(cheroke_2004.capacidad))
print("asientos= "+str(cheroke_2004.asientos))
print("color= "+str(cheroke_2004.color))
print(cheroke_2004.aire)
print("volante= "+str(cheroke_2004.volante))
print("frenos= "+str(cheroke_2004.frenos))

cheroke_2004.encender()
cheroke_2004.apagar()
cheroke_2004.velocidad_maxima()
cheroke_2004.arrancar_control()
