class estudiante:
   
  "atributos"
  uniforme= 1
  mochila = 1
  libros= 6
  libretas= 6
  utiles= "lapices, lapiceros"

  "atributos" 
  def __init__(self):
     print("Constructor estudiante")
     print("uniforme= "+str(self.uniforme))
     print("mochila "+str(self.mochila))
     print("libros= "+str(self.libros))
     print("libretas= "+str(self.libretas))
     print("utiles= "+str(self.utiles))

  
  
  "métodos"
  def estudiar(self):
    print("estudiar")

  def leer(self):
    print("leér")
    
    

class estudiante_prepa(estudiante):  
  
  def __init__(self):
    print("constructor de banco Azteca")
    print("cajeros= "+str(self.cajeros))
    print("personal= "+str(self.personal))
    print("sillas= "+str(self.sillas))
    print("pantallas llama turnos= "+str(self.pantallas_llama_turnos))
    print("ventanillas= "+str(self.ventanillas))



objeto = estudiante()
objeto.estudiar()
objeto.leer()

objeto_estudiante_prepa = estudiante_prepa()
objeto_estudiante_prepa.estudiar()
objeto_estudiante_prepa.leer()