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
    print("constructor estudiantes de preparatoria")
    pass

CBTIS = estudiante_prepa()

print("Uniforme= "+str(CBTIS.uniforme))
print("mochila= "+str(CBTIS.mochila))
print("libros= "+str(CBTIS.libros))
print("libretas= "+str(CBTIS.libretas))
print("utiles= "+str(CBTIS.utiles))
print(CBTIS.estudian_algebra)
print(CBTIS.carrera)

CBTIS.estudiar()
CBTIS.leer()
CBTIS.dormir_tarde()
CBTIS.trabajos()