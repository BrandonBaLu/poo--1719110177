import unidecode  
class palindromo: 
  texto =""
  vocales="aeiou" 

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

  def vocal(self):
    global texto
  def vocales(self):
    vocal=["a","e","i","o","u","á","é","í","o","ú"]
    cont=0
    for i in vocal:
      for j in texto:
        if (1==j):
          cont+=1
    print("elnumero de vocales es: ",cont)

    
eleccion="S"
while  eleccion=="S" or eleccion=="s":
  texto =input("Ingresa el texto:\n") 
  if texto.isalpha() == True:
    texto=unidecode.unidecode(texto)
  print(texto)
  objetopalindromo= palindromo(texto)
  objetopalindromo.palindromo()
  objetopalindromo.vocal()
  objetopalindromo.vocales()
  eleccion=input("¿Desea analizar otra cadena s/n\n")