class seriestv:
  '''Atríbutos'''

  accion= "series de aventuras disparos"
  drama= "series de tristeza"
  romance= "series de amor"
  terror= "series de terror para los amantes a ello"
  ciencia_ficcion= "series de fantasia"
  comedias= "tevenovelas para la familia"
  reality= "series de reality show"
  emocion= "mucha emocion y suspenso"
  favoritas= "lista de tus series favoritas"
  descargas="descargar"
 
  '''Métodos'''
  def entretenerse(self):
    print("matar el aburrimiento")
  def convivir(self):
    print("convivir en familia viendo las series")
  def actuar(self):
    print("actuar")
  def grabar(self):
    print("grabar")
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