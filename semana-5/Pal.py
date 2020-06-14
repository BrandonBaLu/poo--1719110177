import unidecode  #importe la libreria que necesitaba para que lea los caracteres  
class palindromo: #inserte la clase llamada palindromo
  texto =""#declare mis variables donde se guardara el texto que ingrese el usuario, declare las vocales e iguale otra variable de texto para continuar programando
  vocales="aeiou" 
  txt=texto 
  espacios=" "#declare la variable espacios que ocuparia en mi ciclo que contara el numero de espacios que hay

  def __init__(self,texto): #definí mi constructor  texto
    self.texto=texto1  #igaule mi variable texto a otra variable que mas abajo ocupe para otras funciones 
    self.texto=texto1.replace(" ", "").lower().replace(".","") #remplace los espacios, puntos y mayusculas a minusculas

   
  
  def palindromo(self): #definí mi funcion palindromo 
    
    lista1=[] #declare dos listas que guardara los caracteres 
    listaux=[]
   
    cont=0 #definí mis contadores en forma global
    contador1=0
    aux=0 
    resultado="" #variables globales
    
    for indice in range(len(self.texto)): #inicie un blucle en un rango del texto que el usuario ingrese 
      caracter = self.texto[indice] #dentro de mi variable indice iguale mis caracteres con texto
      lista1.append(caracter)  #listas globales 
      listaux.append(caracter)
      cont=cont+1  #aumente mi contador 
    for i in range(cont-1,-1,-1): 
      if lista1[aux]==listaux[i]:
        resultado="Es palindromo"
      else:
        resultado="No palindromo"
        def test():
          
          return texto

        test()


      aux=aux+1
      
    print(resultado)



  def vocales(self):
    vocal=["a","e","i","o","u","á","é","í","ó","ú"] 
    cont=0
    for i in vocal:
      for j in txt:
        if (i==j):
          cont+=1
    print("el numero de vocales es: ",cont)


    
repetir="S"
while  repetir=="S" or repetir=="s":
  texto =input("Ingresa el texto a analizar:\n").lower().replace(".","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
  txt=texto
  texto1=texto
  print ("El texto es:",txt)
  contador1=0 
  for espacios in txt:
     if espacios in " ":
      contador1+=1
  print("El total de espacios dentro del texto es:",contador1)   
  
  if texto.isalpha() == True: #evalúe si es verdad que iterara los 
    texto=unidecode.unidecode(texto1)
  objetopalindromo= palindromo(texto1)
  objetopalindromo.palindromo()
  objetopalindromo.vocales()
  repetir=input("¿Desea analizar otra cadena s/n\n")