class cesar:
 texto=input ("tu texto:  ")
 if texto==texto.upper () : #PARA MAYUSCULAS
 
      abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
 
 else:
 
      abc="abcdefghijklmnñopqrstuvwxyz" #PARA MINUSCULAS 
 #DEFINIMOS VALOR DE DESPLAZAMIENTO
k=int (input ("Valor de desplazamiento: "))
 
#CREAMOS LA CADENA "cifrad".
cifrad=""
 
#REALIZAMOS CIFRADO.
for c in texto:
 if c in abc:
  cifrad += abc((abc.index(c)+k%(len(abc)))
