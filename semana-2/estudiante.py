class estudiante:
  '''Atríbutos'''

  nombre= "Brandon Balderas Lucas"
  matricula= "1719110177"
  cursa= "ingenieria en Tics"
  grupo= "tic 22"
  promedio= "9.66"
  materias= "7"
  regular= "si"
  taller= "guitarra"
  computadoras= "1"
  impresoras="1"
 
  '''Métodos'''
  def estudiar(self):
    print("estudiar una carrera")
  def entregar(self):
    print("entregar tareas")
  def calificar(self):
    print("calificar")
  def reinscribirse(self):
    print("reinscribirse")
  def pagar(self):
    print("pagar en el banco")  

  def _init_(self):
    print("atributos de un alumno")
    print("Nombre="+str(self.nombre))
    print("Matricula"+str(self.matricula))
    print("Cursa="+str (self.cursa))
    print("grupo="+str(self.grupo))
    print("promedio="+str(self.promedio))
    print("materias="+str(self.materias))
    print("regular="+str(self.regular))
    print("taller="+str(self.taller))
    print("computadoras="+str(self.computadoras))
    print("impresoras="+str(self.impresoras))
objeto = estudiante()
objeto.estudiar()
objeto.entregar()
objeto.calificar()
objeto.reinscribirse()
objeto.pagar()
objeto._init_()
