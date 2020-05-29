class classroom:
 Color="anaranjado"
 Correo="1719110177@utectulancingo.edu.mx"
 nombre_del_alumno="Brandon Balderas Lucas"
 Institucion="UTEC"
 Numero_tareas= "10"
 Publicacion_tarea= "Lunes"
 Fecha_entrega=" Domingo"


 '''Metodos'''
 def Entregar(self): 
   print("Entregar")
 def Publicar_tarea(self):
   print("Publicar Tareas")
 def Ver_calificacion(self):
   print("calificar")
 def Compartir_archivos(self):
   print("Compartir ")
 def Comentar(self):
   print("Comentar")
 
 def _init_(self):
   print("Color: "+str(self.Color))
   print("Correo: "+str(self.Correo))
   print("Institucion: "+str(self.Institucion))
   print("Numero de tareas: "+str(self.Numero_tareas))
   print("Publicacion de tarea: "+str(self.Publicacion_tarea))
   print("Fecha de entrega: "+str(self.Fecha_entrega))
   print("nombre del alumno:"+ str(self.nombre_del_alumno))


objeto=classroom()
objeto._init_()
objeto.Entregar()
objeto.Publicar_tarea()
objeto.Ver_calificacion()
objeto.Compartir_archivos()
objeto.Comentar()