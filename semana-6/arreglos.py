class arreglos():#Definí mi clase 
    
    arreglo=[] #declare mi variable global
    
    def _init_(self) :
        pass
            
    def leer(self) :#Definí mi metodo
        nombre=input("ingresar el nombre completo del alumno\n") #pedí al usuario el nombre del alumno 
        nacimiento =int(input("Año de nacimiento\n"))#pedí al usuario el año de nacimiento del alumno
        grupo=input("ingresa el grupo\n") #Pedí el grupo del alumno
        edad=2020-nacimiento#realice mi operación que calcula la edad de los usuarios 
        datos=[nombre, grupo, edad]#ocupe otro arreglo para meter mis valores pedidos
        self.arreglo.append(datos)#guarde mis valores en mi variable global
        
    def imprimir(self) :#Declare mi metodo para imprimir 
        for fila in self.arreglo:#En un rango de lo que los valores de arreglos tenga imprime sus valores
            print ("¦El alumno es:", fila[0]+ " ¦su grupo es: ", fila[1 ]+ " ¦su edad es de: ", fila[2])#Imprime los valores del arreglo de acorde a las poscisiones que se le pide. 
        
    
objeto=arreglos() #iguale mi variable objeto a arreglos
repetir= "S" #declare mi variable repetir  
while True:#mientras sea verdad la respuesta del usuario repetira el proceso de leer los valores que ingrese el usuario 
    if repetir == "S" or repetir =="s" :
        objeto.leer()#se ejecuta el metodo leer. 
        repetir =input("¿Desea agregar a otro alumno?\n") #pregunto si el usuario desea agregar otro usuario si la respuesta es si, vuelve a pedir los valores
    if repetir=="n" or repetir =="N":#si la respuesta es no, ejecuta el metodo imprimir, e imprime los resultados 
        objeto.imprimir()#ejecuta el metodo impromir. 
        print ("Gracias por usar tu app Escuela segura") 
        break