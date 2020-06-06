class classroom:
   
  #atríbutos
  Color="anaranjado"
  Correo="1719110177@utectulancingo.edu.mx"
  nombre_del_alumno="Brandon Balderas Lucas"
  Institucion="UTEC"
  Numero_tareas= "10"
  
  #métodos

  def Ver_calificacion(self):
   print("calificar")
  
  def Compartir_archivos(self):
   print("Compartir ")
  
  def Comentar(self):
   print("Comentar")
  
  def __init__(self):
    pass

        

class classrom_salvador(classroom):
  
  #atríbutos
  
  Publicacion_tarea= "Lunes"
  Fecha_entrega= "Domingo"

  #métodos
  
  def Entregar(self): 
   print("Entregar")
  
  def Publicar_tarea(self):
   print("Publicar Tareas")

  def __init__(self):
    print("constructor classrom POO")
  
  def Ver_calificacion(self):
   print("calificar tareas del alumno")
  
  def Compartir_archivos(self):
   print("Compartir archivos para el alumno ")
  
  def Comentar(self):
   print("Comentar indicacionespara el alumno")
  
  def Entregar(self): 
   print("Entregar tareas por parte del alumno")
  
  def Publicar_tarea(self):
   print("Publicar Tareas")
   pass

classroom_poo = classrom_salvador()

print("Color de la clase de POO: "+str(classroom_poo.Color))
print("Correo del alumno inscrito : "+str(classroom_poo.Correo))
print("Institucion del alumno: "+str(classroom_poo.Institucion))
print("Numero de tareas asignadas en POO: "+str(classroom_poo.Numero_tareas))
print("Publicacion de tarea en POO: "+str(classroom_poo.Publicacion_tarea))
print("Fecha de entrega de las tareas asignadas de POO: "+str(classroom_poo.Fecha_entrega))
print("nombre del alumno inscrito a la clase de POO:"+ str(classroom_poo.nombre_del_alumno))


classroom_poo.Entregar()
classroom_poo.Publicar_tarea()
classroom_poo.Ver_calificacion()
classroom_poo.Compartir_archivos()
classroom_poo.Comentar()