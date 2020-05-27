class classroom:
 Color="anaranjado"
 Correo="1719110177@utectulancingo.edu.mx"
 Institucion="UTEC"
 Numero_tareas= "10"
 Publicacion_tarea= "Lunes"
 Fecha_entrega=" Domingo"

 '''Metodos'''
 def Entregar(self): 
   print("Entregar")
 def Publicar_tarea(self):
   print("Publicar_Tarea")
 def Ver_calificacion(self):
   print("Ver_calificacion")
 def Compartir_archivos(self):
   print("Compartir_archivos")
 def Comentar(self):
   print("Comentar")
 
 def _init_(self):
   print("Color: {}".format(self.Color))
   print("Correo: {}".format(self.Correo))
   print("Institucion: {}".format(self.Institucion))
   print("Numero_tareas: {}".format(self.Numero_tareas))
   print("Publicacion_tarea: {}".format(self.Publicacion_tarea))
   print("Fecha_entrega: {}".format(self.Fecha_entrega))


objeto=classroom()
objeto._init_()
objeto.Entregar()
objeto.Publicar_tarea()
objeto.Ver_calificacion()
objeto.Compartir_archivos()
objeto.Comentar()