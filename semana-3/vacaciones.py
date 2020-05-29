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
  
  trajes_de_baño="estudian algebra"
  caminar="caminar en la arena"

  #métodos

  def  divertirse(self):
    print("crear actividades divertidas")
 
  def jugar(self):
    print("algun juego emocionante para tí"")

  def __init__(self):
    print("constructor de vacaciones en la playa")
    pass

riviera_maya = estudiante_prepa()

print("Uniforme= "+str(riviera_maya.uniforme))
print("mochila= "+str(riviera_maya.mochila))
print("libros= "+str(riviera_maya.libros))
print("libretas= "+str(riviera_maya.libretas))
print("utiles= "+str(riviera_maya.utiles))
print(riviera_maya.estudian_algebra)
print(riviera_maya.carrera)

riviera_maya.estudiar()
riviera_maya.leer()
riviera_maya.dormir_tarde()
riviera_maya.trabajos()