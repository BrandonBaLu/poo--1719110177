import unidecode  
class palindromo: 
  texto =""
  vocales="aeiou" 
  txt=texto 
  espacios=" "

  def __init__(self,texto): 
    self.texto=texto1    
    self.texto=texto1.replace(" ", "").lower().replace(".","")

   
  
  def palindromo(self):
    
    lista=[]
    listaaux=[]
   
    cont=0
    contador1=0
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
  texto =input("Ingresa el texto:\n").lower().replace(".","").replace("á","a")
  txt=texto
  texto1=texto
  print ("El texto es:",txt)
  contador1=0 
  for espacios in txt:
     if espacios in " ":
      contador1+=1
  print("El total de espacios dentro del texto es:",contador1)   
  
  if texto.isalpha() == True:
    texto=unidecode.unidecode(texto1)
  objetopalindromo= palindromo(texto1)
  objetopalindromo.palindromo()
  objetopalindromo.vocales()
  repetir=input("¿Desea analizar otra cadena s/n\n")