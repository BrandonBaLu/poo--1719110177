class avion:
  '''Atríbutos'''

  alas="2"
  asientos= "48"
  baños= "2"
  ventanas= "60"
  ruedas= "2"
  cabinas= "1"
  cocina= "1"
  volantes= "1"
  microfonos= "6"
  pilotos="2"
 
  '''Métodos'''
  def despegar(self):
    print("despegar")
  def volar(self):
    print("volar")
  def viajar(self):
    print("viajar")
  def relajarse (self):
    print("relajarse en el avíon")
  def aterrizar(self):
    print("aterrizar")  

  def _init_(self):
    print("atributos de un avíon")
    print("alas="+str(self.alas))
    print("asientos"+str(self.asientos))
    print("baños="+str (self.baños))
    print("ventanas="+str(self.ventanas))
    print("ruedas="+str(self.ruedas))
    print("cabinas de pilotos ="+str(self.cabinas))
    print("cocina="+str(self.cocina))
    print("volantes="+str(self.volantes))
    print("microfonos ="+str(self.microfonos))
    print("pilotos="+str(self.pilotos))
objeto = avion()
objeto.despegar()
objeto.volar()
objeto.viajar()
objeto.relajarse()
objeto.aterrizar()
objeto._init_()