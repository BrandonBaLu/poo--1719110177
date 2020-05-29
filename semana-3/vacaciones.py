class vacaciones:
   
  "atríbutos"
  jugar= "con la familia"
  trajes de baño= 15
  lugares_relajantes= "en lugares relajantes"
  divertirse= "crear actividades divertidas"
  gastronomia= "comidas tipicas del lugar"
  
  #métodos

  def relajarse(self):
    print("relajarse")

  def descansar(self):
    print("descansar")

  
  def __init__(self):
    pass

        

class estudiante_prepa(estudiante):
  
  #atríbutos
  
  estudian_algebra="estudian algebra"
  carrera="carrera tecnica"

  #métodos

  def  dormir_tarde(self):
    print("dormir tarde")

  def trabajos(self):
    print("proyectos")

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