class estudiante:
   
  "atríbutos"
  uniforme= 1
  mochila = 1
  libros= 6
  libretas= 6
  utiles= "lapices, lapiceros"
  
  #métodos

  def estudiar(self):
    print("estudiar")

  def leer(self):
    print("leér")

  
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
    print("constructor estudiantes de CBTIS")
  uniforme= "color azul"
  libros= "por materia"
  libretas= "por materia"
  utiles= "material didactico"
  def estudiar(self):
    print("estudiar en las instalaciones del CBTIS")

  def leer(self):
    print("leér en el CBTIS")
  
  def  dormir_tarde(self):
    print("dormir tarde por realizar tareas")

  def trabajos(self):
    print("proyectos del CBTIS")

  def entrar(self):
    print("entrar temprano al CBTIS")
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
CBTIS.entrar