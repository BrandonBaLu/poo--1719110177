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
    pass

classroom_poo = classrom_salvador()

print("Color: "+str(classroom_poo.Color))
print("Correo: "+str(classroom_poo.Correo))
print("Institucion: "+str(classroom_poo.Institucion))
print("Numero de tareas: "+str(classroom_poo.Numero_tareas))
print("Publicacion de tarea: "+str(classroom_poo.Publicacion_tarea))
print("Fecha de entrega: "+str(classroom_poo.Fecha_entrega))
print("nombre del alumno:"+ str(classroom_poo.nombre_del_alumno))


classroom_poo.Entregar()
classroom_poo.Publicar_tarea()
classroom_poo.Ver_calificacion()
classroom_poo.Compartir_archivos()
classroom_poo.Comentar()3