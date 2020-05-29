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

        

class estudiante_prepa(estudiantes):
  
  #atríbutos
  
  estudian_algebra="estudian algebra"
  carrera="carrera tecnica"

  #métodos

  def  dormir_tarde(self):
    print("dormir tarde")

  def trabajos(self):
    print("proyectos")

  def __init__(self):
    pass

CBTIS = estudiante_prepa()

print("abierto hasta las= "+str(elektra.abierto_tarde))
print(elektra.entrega)
print("cajeros= "+str(elektra.cajeros))
print("personal= "+str(elektra.personal))
print("sillas= "+str(elektra.sillas))
print("pantallas llama turnos= "+str(elektra.pantallas_llama_turnos))
print("ventanillas= "+str(elektra.ventanillas))

elektra.estudiar()
elektra.leer()
elektra.dormir_tarde()
elektra.carrera()