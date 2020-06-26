class cesar:#primero declare mi clase

  def _init_(self):#definí mi constructor
    pass

  def ascii(self): #por otro lado definí mi metodo en donde se generara el cifrado
    texto =input("ingresa tu texto\n")#pedi que el usuario ingresara su cadena de texto
    for texto in texto:#en un rango de lo que mide la cadena pedi que codificara el texto
      print("El valor de {} es {}".format(texto, ord(texto)))
  
  def descodificar (self):#declare mi metodo descodificar que se encarga de realizar dicha funcion
    numeros=int(input("ingresa tus valores en numeros enteros\n"))
    for numero in numeros:#con ayuda de el for 
      print("El carácter que representa a {} es {}".format(numero, chr(numero)))#imprimo los valores y los convierto los valores en letras de nuevo, aunque no me sale ;(

repetir="s"#declaro mi variable de repetir
while repetir=="s" or repetir=="S":#inicio mi ciclo de iteracion para preguntarle al usuario que si quiere realizar otra operacion
  objetoCesar = cesar()#iguale mi bojeto con mi clase 
  tipo=int(input("¿Que deseas hacer?\n¦1:cifrar¦\n¦2:descifrar¦\ningresa el numero de lo que deseas hacer\n"))# pregunto al usuario que desea hacer y que elija con un numero de lo que desea hacer
  if tipo==1:#si el usuario elije la opccion 1 le digo que realice todo lo que esta en el metodo ascii
    objetoCesar.ascii()
  if tipo==2:#si el usuario elije la opccion  le digo que realice todo lo que esta en el metodo descodificar
    objetoCesar.descodificar()
  repetir=input ("¿Desea repetir? S/N\n")#pregunto al usuario si desea repetir
  