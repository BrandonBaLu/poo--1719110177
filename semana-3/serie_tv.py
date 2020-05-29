class seriestv:
   
  "atríbutos"
  accion= "series de aventuras disparos"
  drama= "series de tristeza"
  romance= "series de amor"
  terror= "series de terror para los amantes a ello"
  ciencia_ficcion= "series de fantasia"
  
  #métodos

  def entretenerse(self):
    print("matar el aburrimiento")
  
  
  def convivir(self):
    print("convivir en familia viendo las series")

  
  def __init__(self):
    pass

        

class series_drama(seriestv):
  
  #atríbutos
  
  emocion= "mucha emocion "
  suspenso="suspenso"

  #métodos

  def actuar(self):
    print("actuar")
  
  def grabar(self):
    print("grabar")

  def __init__(self):
    print("constructor de SexEducation ")
    pass

SexEducation = series_drama()

print("accion = "+str(SexEducation.accion))
print("drama = "+str(SexEducation.drama))
print("romance= "+str(SexEducation.romance))
print("terror= "+str(SexEducation.terror))
print(SexEducation.ciencia_ficcion)
print(SexEducation.emocion)
print(SexEducation.suspenso)

SexEducation.relajarse()
riviera_maya.descansar()
riviera_maya.nadar()
riviera_maya.bucear()




class :
  '''Atríbutos'''

  
  comedias= "tevenovelas para la familia"
  reality= "series de reality show"
  
  favoritas= "lista de tus series favoritas"
  descargas="descargar"
 
  '''Métodos'''
  
  
  def peleas(self):
    print("peleas ficticias")  

  def _init_(self):
    print("atributos de un alumno")
    print(self.accion)
    print(self.drama)
    print(self.romance)
    print(self.terror)
    print(self.ciencia_ficcion)
    print(self.comedias)
    print(self.reality)
    print(self.emocion)
    print(self.favoritas)
    print(self.descargas)
objeto = seriestv()
objeto.entretenerse()
objeto.convivir()
objeto.actuar()
objeto.grabar()
objeto.peleas()
objeto._init_()