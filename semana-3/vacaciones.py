class vacaciones:
   
  "atríbutos"
  juegos_didacticos="juegos didacticos"
  familia= "personas con quien disfrutes estar"
  lugares_relajantes= "en lugares relajantes"
  comidas_en_familia="comer con la familia"
  gastronomia= "comidas tipicas del lugar"
  
  #métodos

  def relajarse(self):
    print("relajarse")

  def descansar(self):
    print("descansar")

  
  def __init__(self):
    pass

        

class vacaciones_playa(vacaciones):
  
  #atríbutos
  
  trajes_de_baño="trajes de baño"
  animales_marinos="tiburones, delphines"

  #métodos

  def  nadar(self):
    print("nadar")
 
  def bucear(self):
    print("bucear")

  def __init__(self):
    print("constructor de vacaciones en la playa de la Riviera  Maya ")
    pass

riviera_maya = vacaciones_playa()

print("juegos = "+str(riviera_maya.juegos_didacticos))
print("familia = "+str(riviera_maya.familia))
print("lugares relajantes= "+str(riviera_maya.lugares_relajantes))
print("comidas en familia= "+str(riviera_maya.comidas_en_familia))
print(riviera_maya.gastronomia)
print(riviera_maya.trajes_de_baño)
print(riviera_maya.animales_marinos)

riviera_maya.relajarse()
riviera_maya.descansar()
riviera_maya.nadar()
riviera_maya.bucear()