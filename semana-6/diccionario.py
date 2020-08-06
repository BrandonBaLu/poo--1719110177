peliculas=[]#declare mis variables globales 
genero=[] 
   
class pelis():#definí mi clase
    
   

    def __init__(self ) :
        pass
        
    def leer(self) :#Definí mi metodo
        print ("===================================================")
        print ("======*UNIVERSIDAD TECNOLÓGICA DE TULANCINGO*======")
        print ("===================================================") 
        nombre=input("========¦Ingresar el nombre de la película:¦=======\n") #pedí al usuario el nombre del alumno 
        try:
            lanzamiento =int(input("==============¦Año de lanzamiento :¦===============\n")) #pedí al usuario el año de nacimiento del alumno
            generos=(input("=======¦Ingresa el genero de la película¦==========\n")) #Pedí el grupo del alumno
            datos=[nombre, genero, lanzamiento ]#utilice mi otro arreglo
            peliculas.append("¦===El nombre de la pelicula es: "+str(nombre)+"===¦"+"=== El año de lanzamiento es: "+str(lanzamiento )+"===¦") #añade al arreglo el nombre y el año de estreno
            genero.append(generos)
            
        except ValueError:
            print("¡¡¡solo se aseptan numeros!!!")
            
     
    def imprimir(self): #definí mi metodo para imprimir 
        datos=dict(zip(peliculas,genero)) #crea un diccionario usando los arreglos creados
        print(datos) #imprime el diccionario
        buscar=input("imgresa el genero de una pelicula:\n") #pide el genero para buscarlo
        if buscar in datos.values(): #si el nombre del genero esta el los valores del diccionario
            for lista in datos: #lee el diccionario
                if datos[lista]==buscar: #condición para buscar el genero
                    print(lista) #imprime la pelicula o películas guardada en el genero ingresado

   
objeto=pelis() #iguale mi variable objeto a arreglos
repetir= "S" #declare mi variable repetir  
while True:#mientras sea verdad la respuesta del usuario repetira el proceso de leer los valores que ingrese el usuario 
    if repetir == "S" or repetir =="s" :
        objeto.leer()#se ejecuta el metodo leer. 
        repetir =input("¿Desea agregar a otra película ? (S/N)\n") #pregunto si el usuario desea agregar otro usuario si la respuesta es si, vuelve a pedir los valores
    if repetir=="n" or repetir =="N":#si la respuesta es no, ejecuta el metodo imprimir, e imprime los resultados 
        objeto.imprimir()#ejecuta el metodo imprimir. 
        print ("Gracias por usar tu app Pelis") 
        break     
 