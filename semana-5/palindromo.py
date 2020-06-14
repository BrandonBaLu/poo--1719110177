import unidecode  
class palindromo: 
  texto ="" #Atributos

  def __init__(self,texto): 
    self.texto=texto    
    print("el texto es: "+self.texto)
    
    self.texto=texto.replace(" ", "").lower().replace(".","")
  
  def palindromo(self):
    
    lista=[]
    listaaux=[]
   
    cont=0
    aux=0
    resultado=""
    
    for indice in range(len(self.texto)):
      caracter = self.texto[indice]
      lista.append(caracter)
      listaaux.append(caracter)
      cont=cont+1 
    for i in range(cont-1,-1,-1): 
      if lista[aux]==listaaux[i]:
        resultado="Es palindromo"
      else:
        resultado="No palindromo"
      aux=aux+1
      
    print(resultado)
eleccion="S"
while  eleccion=="S" or eleccion=="s":
  texto =input("Ingresa la palabra:\n") 
  if texto.isalpha() == True:
    texto=unidecode.unidecode(texto)
  print(texto)
  objetopalindromo= palindromo(texto)
  objetopalindromo.palindromo()
  eleccion=input("¿Desea analizar otra cadena s/n\n")

    
    
