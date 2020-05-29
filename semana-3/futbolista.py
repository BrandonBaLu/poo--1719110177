class futbolista:
   
  "atríbutos"
  edad= 22
  altura= 1.80
  camiseta= 1
  posicion= "delantero"
  categoria="juvenil"
  
  #métodos

  def correr(self):
    print("correr")
  
  
  def saltar(self):
    print("saltar")
  
  def __init__(self):
    pass

        


class futbolista_barcelona(futbolista):
  
  #atríbutos
  
  messi= "Lionel Messi "
  calidad="calidad de jugadores"

  #métodos

   def patear(self):
    print("patear")
  
  def gol(self):
    print("meter gol")

  def __init__(self):
    print("constructor de SexEducation ")
    pass

SexEducation = series_drama()

print("accion = "+str(SexEducation.accion))
print("drama = "+str(SexEducation.drama))
print("romance= "+str(SexEducation.romance))
print("terror= "+str(SexEducation.terror))
print(SexEducation.ciencia_ficcion)
print(SexEducation.emocion)
print(SexEducation.suspenso)

SexEducation.entretenerse()
SexEducation.convivir()
SexEducation.actuar()
SexEducation.grabar()

class futbolista:
  edad= 22
  altura= 1.80
  camiseta= 1
  posicion= "delantero"
  categoria="juvenil"
  nombre= "Brandon BaLu"
  
  
 
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