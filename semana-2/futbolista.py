class futbolista:
  edad= 22
  altura= 1.80
  camiseta= 1
  posicion= "delantero"
  categoria="juvenil"
  nombre= "Brandon BaLu"
  
  def correr(self):
    print("correr")
  def saltar(self):
    print("saltar")
  def patear(self):
    print("patear")
  def gol(self):
    print("meter gol")
  def festejar(self):
    print("festejar")
 
  def _init_(self):
    print("Futbolista")
    print(self.edad)
    print(self.altura)
    print(self.camiseta)
    print(self.posicion)
    print(self.categoria)
    print(self.nombre)

objeto = futbolista()
objeto.correr()
objeto.saltar()
objeto.patear()
objeto.gol()
objeto.festejar()
objeto._init_()