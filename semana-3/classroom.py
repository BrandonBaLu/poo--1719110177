class classroom:
   
  "atríbutos"
  Color="anaranjado"
  Correo="1719110177@utectulancingo.edu.mx"
  nombre_del_alumno="Brandon Balderas Lucas"
  Institucion="UTEC"
  Numero_tareas= "10"
  
  #métodos

  def prender(self):
    print("Encender")

  def apagar(self):
    print("apagar")

  
  def __init__(self):
    pass

        

class classrom_salvador(classroom):
  
  #atríbutos
  
  Publicacion_tarea= "Lunes"
  Fecha_entrega=" Domingo"

  #métodos
  
  def  graficar(self):
    print("graficar")
    
  def dividir(self):
    print("dividir")

  def __init__(self):
    print("constructor de calculadora casio_126Clc")
    pass

casio_126Clc = casio()

print(casio_126Clc.funciones)
print(casio_126Clc.multiplicacion)
print("teclas= "+str(casio_126Clc.teclas))
print("tipo= "+str(casio_126Clc.tipo))
print("forma "+str(casio_126Clc.forma))
print("funciones casio 126Clc= "+str(casio_126Clc.funciones_c))
print("color= "+str(casio_126Clc.color))



casio_126Clc=casio()
casio_126Clc.prender()
casio_126Clc.apagar()
casio_126Clc.graficar()
casio_126Clc.dividir()
 
 

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