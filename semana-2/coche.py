class coche:
  placas= "hkk5846"
  modelo=2005
  puertas=4
  capasidad= 5
  asientos=6
  color= "AMARILLO"
  aire= "con aire acondicionado"
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