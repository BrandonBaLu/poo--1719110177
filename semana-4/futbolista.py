class futbolista:
   
  "atríbutos"
  edad= 17
  altura= 1.80
  camiseta= 10
  posicion= "delantero"
  categoria="libre"
  
  #métodos

  def correr(self):
    print("correr")
  
  
  def saltar(self):
    print("saltar")
  
  def __init__(self):
    pass

        


class futbolista_barcelona(futbolista):
  
  #atríbutos
  
  plantilla_jugadores= "plantilla de jugadores "
  calidad="calidad de jugadores"

  #métodos

  def patear(self):
    print("patear")
  
  def gol(self):
    print("meter goles")

  def __init__(self):
    print("Lionel Messi ")
  
  def correr(self):
    print("correr  a una velocidad de 32.5 Km/h")
  edad= "32 años"
  altura= 1.70
  camiseta= 10
  posicion= "delantero"
  categoria="libre"
  
  def saltar(self):
    print("salta a una altura de 2.56 metros ")

  def patear(self):
    print("patea a 119 km/h")
  
  def gol(self):
    print("mete un promedio de goles de 0.81% por partido")
    pass

Messi = futbolista_barcelona()

print("edad = "+str(Messi.edad))
print("altura = "+str(Messi.altura))
print("camiseta= "+str(Messi.camiseta))
print("posicion= "+str(Messi.posicion))
print("categoria= "+str(Messi.categoria))
print(Messi.plantilla_jugadores)
print(Messi.calidad)

Messi.correr()
Messi.saltar()
Messi.patear()
Messi.gol()

