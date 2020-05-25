class vacaciones:
  '''Atríbutos'''

  ropa= "ropa comoda"
  lugares= "destino a vacacionar"
  familia= "convivir en familia"
  hotel= "trivago"
  gastronomia= "cultural"
  dinero= "reservar dinero"
  relajarse= "si"
  caminar= "por la playa"
  recuerdos= "fotografias"
  cenar="bajo la luz de la luna"
 
  '''Métodos'''
  def viajar(self):
    print("viajar a destinos turisticos")
  def relajarse(self):
    print("relajarse en lugares calidos")
  def comunicarse(self):
    print("comunicarse con la familia y disfrutarla")
  def jugar(self):
    print("jugar y reir mucho")
  def disfrutar(self):
    print("disfrutar las vacaciones")  

  def _init_(self):
    print("atributos de las vacaciones")
    print("ropa ="+str(self.ropa))
    print("lugares"+str(self.lugares))
    print("familia="+str (self.familia))
    print("hotel="+str(self.hotel))
    print("gastronomia="+str(self.gastronomia))
    print("dinero="+str(self.dinero))
    print("relajarse="+str(self.relajarse))
    print("taller="+str(self.taller))
    print("computadoras="+str(self.computadoras))
    print("impresoras="+str(self.impresoras))
objeto = estudiante()
objeto.estudiar()
objeto.entregar()
objeto.calificar()
objeto.reinscribirse()
objeto.pagar()
objeto._init_()